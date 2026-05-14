import pyautogui #Ele da a cordenada do meu cursosr toda hora

try:
    while True:
        x, y = pyautogui.position()
        print(x, y)

except KeyboardInterrupt:
    print('\nDone.') #Quando der um ctrl C ele trava