import pyautogui
import time
import subprocess

if 'active' == subprocess.check_output("gnome-screensaver-command -q", shell=True).decode('utf-8').split()[3]:
    pyautogui.moveTo(960, 540)
    time.sleep(1)
    pyautogui.write('6x27y27z2', interval=0.25)
    pyautogui.press('enter')
    time.sleep(2)

#ABRIR CHROME E AHGORA
subprocess.Popen("/usr/bin/google-chrome --start-maximized", shell=True)
time.sleep(1)

pyautogui.moveTo(1765, 80)
pyautogui.click()

#ENTRADA DE DADOS AHGORA
pyautogui.moveTo(1350, 220)
pyautogui.click()
pyautogui.write('01924', interval=0.25) 
pyautogui.moveTo(1350, 295)
pyautogui.click()
pyautogui.write('teste', interval=0.25)

#CONFIRMAR E FECHAR
pyautogui.moveTo(1600, 335)
pyautogui.click()
time.sleep(2)

pyautogui.moveTo(1900, 45)
pyautogui.click()
