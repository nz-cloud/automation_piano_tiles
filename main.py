import pyautogui
import time
import keyboard
import random
import win32api, win32con


#position 1 = x: 513  y:367 RGB:(0, 0, 0)
#position 2 = x: 627  y:367 RGB:(0, 0, 0)
#position 3 = x: 732  y:367 RGB:(0, 0, 0)
#position 4 = x: 848  y:367 RGB:(0, 0, 0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    if pyautogui.pixel( 513, 367)[0] == 0:
        click(513, 367)
    if pyautogui.pixel(627, 367)[0] == 0:
        click(627, 367)
    if pyautogui.pixel(732, 367)[0] == 0:
        click(732, 367)
    if pyautogui.pixel(848, 367)[0] == 0:
        click(848, 367)