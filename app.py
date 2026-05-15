import webbrowser  # Biblioteca para abrir janela
import pyautogui   # Biblioteca para mover o mouse
from time import sleep

# Abrir o navegador
webbrowser.open('http://tiktok.com') 
sleep(8)

# Fluxo de Login
pyautogui.click(31, 674, duration=2) # login
sleep(3)
pyautogui.click(319, 462, duration=2) # muda para email
sleep(2)
pyautogui.click(588, 397, duration=2) 
sleep(1)
pyautogui.click(321, 447, duration=2)
pyautogui.write("karlheinz4761@uorak.com")
sleep(2)
pyautogui.click(310, 508, duration=2)
pyautogui.write("j3H,GxYkQSg<[Tg")
sleep(3)
pyautogui.click(436, 627, duration=2)
sleep(5)

# FECHAR A ABA DE LOGIN PARA PARAR O SOM
pyautogui.hotkey('ctrl', 'w') 
sleep(2) 

# Acessar perfil
webbrowser.open('https://www.tiktok.com/@isabellimouraa?lang=en') 
sleep(5)
pyautogui.click(271, 867, duration=2)

# Bloco Try/Except corrigido
while True:
    try:
        # Procura coração vermelho (já curtido)
        curtido = pyautogui.locateOnScreen(
            "curtido.png",
            confidence=0.7
        )

        # Se encontrou -> só desce
        if curtido:
            print("Já curtido")

            pyautogui.press("down")
            sleep(2)

    except:
        # Se NÃO encontrou -> curte
        print("Não curtido")

        pyautogui.click(853, 391, duration=1)

        sleep(1)

        pyautogui.click(712, 391, duration=1)

        pyautogui.press("down")

        sleep(2)