import pyautogui
import time
import os
os.system('cls')
print("starting spam from spam.txt")
time.sleep(5)
f = open("shrek.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
