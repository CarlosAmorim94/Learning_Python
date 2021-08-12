import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1 - Entrar no nosso sistema (entrar no link: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing)
pyautogui.hotkey("ctrl", "t")
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Passo 2 - Navegar no sistema (entrar na pasta Exportar)
time.sleep(5) # espera 5 segundos
pyautogui.click(x=478, y=317, clicks=2)

# Passo 3 - baixar o arquivo de vendas
time.sleep(2)
pyautogui.click(x=524, y=370)
pyautogui.click(x=1110, y=182)
pyautogui.click(x=968, y=724)
time.sleep(3) # esperar fazer o download