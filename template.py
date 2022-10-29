import time
import pyautogui


time.sleep(5)

print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
pyautogui.click(x=2101, y=334, clicks =2)
pyautogui.hotkey('ctrl','r')

pyautogui.moveTo(-581, 482)
time.sleep(20)
pyautogui.click(x=855, y=497)
location0 = pyautogui.locateOnScreen('play.png')
pyautogui.click(location0)


while True:
    time.sleep(20)