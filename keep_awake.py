import ctypes
import pyautogui
import time

# Função para detectar tempo de inatividade
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_time():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
        millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0  # tempo ocioso em segundos
    return 0

# Loop principal do script
while True:
    idle = get_idle_time()
    if idle > 120:  # Se o tempo de inatividade for maior que 2 minutos (120 segundos)
        pyautogui.moveRel(0, 10)  # Move o mouse para baixo
        pyautogui.moveRel(0, -10) # Volta o mouse para cima
        pyautogui.click()         # Simula um clique do mouse
    time.sleep(10)  # Espera 10 segundos antes de checar novamente
