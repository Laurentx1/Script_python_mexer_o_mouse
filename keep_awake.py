import pyautogui
import time

print("ANTI GPU SPIN - FUNCIONANDO!")
print("Vai fazer double clique a cada 2 minutos")
print("Pressione Ctrl+C para parar")

contador = 0

while True:
    try:
        # Espera 2 minutos (120 segundos)
        for i in range(120):
            time.sleep(1)
            contador += 1
            
            # Mostra que está vivo a cada 30 segundos
            if contador % 30 == 0:
                print(f"Rodando... {contador} segundos")
        
        # Faz double clique depois de 2 minutos
        print("FAZENDO DOUBLE CLIQUE!")
        pyautogui.doubleClick()
        print("Pronto! Double clique feito.")
        
        contador = 0  # Reinicia contador
        
    except KeyboardInterrupt:
        print("\nPARADO!")
        break
    except Exception as e:
        print(f"ERRO: {e}")
        print("Continuando mesmo assim...")
        
print("FIM!")
input("Enter para fechar")
