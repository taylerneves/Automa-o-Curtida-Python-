import webbrowser  # Biblioteca para abrir janela
import pyautogui # Biblioteca para mover o mouse
from time import sleep

webbrowser.open('http://tiktok.com') 
sleep(12)
pyautogui.click(305,438,duration=2) #login
sleep(3)
pyautogui.click(574,337,duration=2) #muda para email
sleep(2)
pyautogui.click(490,386,duration=2)
pyautogui.write("karlheinz4761@uorak.com")
sleep(2)
pyautogui.click(297,456,duration=2)
pyautogui.write("j3H,GxYkQSg<[Tg")
sleep(3)
pyautogui.click(480,583,duration=2)