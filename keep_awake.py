import ctypes
import pyautogui
import time

# Estrutura para detectar inatividade
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_time():
    """Retorna tempo de inatividade em segundos"""
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
        millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0
    return 0

def move_mouse():
    """Move o mouse um pouquinho e volta"""
    try:
        # Movimento pequeno para baixo e depois volta
        pyautogui.moveRel(0, 10, duration=0.2)
        time.sleep(0.1)
        pyautogui.moveRel(0, -10, duration=0.2)
        print("Mouse movido!")
    except:
        # Se der erro, só clica
        pyautogui.click()
        print("Clique feito!")

print("=== ANTI GPU SPIN ===")
print("Mantém sua GPU quieta!")
print("Pressione Ctrl+C para parar")
print("Monitorando...")

# Loop principal
try:
    while True:
        tempo_parado = get_idle_time()
        
        # Mostra status de vez em quando
        if int(tempo_parado) % 30 == 0 and tempo_parado > 0:
            print(f"Inativo há {tempo_parado:.0f}s")
        
        # Se parado por mais de 2 minutos (120s), mexe o mouse
        if tempo_parado > 120:
            print(f"AÇÃO! Parado por {tempo_parado:.0f}s")
            move_mouse()
            time.sleep(5)  # Espera 5s depois de mexer
        
        time.sleep(10)  # Verifica a cada 10 segundos

except KeyboardInterrupt:
    print("\nParado! GPU deve ficar quieta agora.")
except Exception as e:
    print(f"Erro: {e}")
    print("Tentando continuar...")

input("Pressione Enter para fechar...")
