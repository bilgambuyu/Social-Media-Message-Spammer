#Limited
import pyautogui
import time
message = 10000
while message > 0:
    time.sleep(2)
    pyautogui.typewrite("Hello! How are you?")
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1

#Unlimited
"""
    time.sleep(2)
    pyautogui.typewrite("Hello! How are you?")
    time.sleep(2)
    pyautogui.press('enter')
"""
