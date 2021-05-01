import os             
import pyautogui
import time
from time import sleep
from datetime import datetime
while(1>0):
    now=datetime.now()
    currtime=now.strftime("%H:%M")
    if(currtime=='11:22'):
        try:
            start=pyautogui.locateCenterOnScreen('start1.png')
            pyautogui.moveTo(start)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite('microsoft teams')
            pyautogui.press('enter')
            time.sleep(2)
            maths=pyautogui.locateCenterOnScreen('maths.png')
            pyautogui.moveTo(maths)
            pyautogui.click()
            time.sleep(2)
            join=pyautogui.locateCenterOnScreen('join.png')
            pyautogui.moveTo(join)
            pyautogui.click()
            time.sleep(1)
            joinnnow=pyautogui.locateCenterOnScreen('joinnnow.png')
            pyautogui.moveTo(joinnow)
            pyautogui.click()
            time.sleep(3660)
            leave=pyautogui.locateCenterOnScreen('leave.png')
            pyautogui.moveTo(leave)
            pyautogui.click()
            break
        except:
            start=pyautogui.locateCenterOnScreen('start1.png')
            pyautogui.moveTo(start)
            pyautogui.click()
            pyautogui.typewrite('notepad')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.typewrite('class cancelled or what???!!')
            break