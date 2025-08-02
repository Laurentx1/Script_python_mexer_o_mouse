import pyautogui
import time

print("ANTI GPU SPIN - DETECÇÃO DE INATIVIDADE!")
print("Double click após 2 minutos de inatividade")
print("Pressione Ctrl+C para parar")

ultima_posicao = pyautogui.position()
tempo_inativo = 0

while True:
    try:
        time.sleep(1)
        posicao_atual = pyautogui.position()
        
        # Se o mouse se moveu, reseta o contador
        if posicao_atual != ultima_posicao:
            tempo_inativo = 0
            ultima_posicao = posicao_atual
        else:
            tempo_inativo += 1
            
            # Mostra status a cada 30 segundos de inatividade
            if tempo_inativo % 30 == 0:
                print(f"Inativo por {tempo_inativo} segundos...")
            
            # Após 2 minutos (120 segundos) de inatividade
            if tempo_inativo >= 120:
                print("FAZENDO DOUBLE CLIQUE!")
                pyautogui.doubleClick()
                print("Pronto! Resetando contador...")
                tempo_inativo = 0
                
    except KeyboardInterrupt:
        print("\nPARADO!")
        break
    except Exception as e:
        print(f"ERRO: {e}")
        
print("FIM!")
input("Enter para fechar")
