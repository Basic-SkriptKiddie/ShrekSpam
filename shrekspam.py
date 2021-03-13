import pyautogui
import time
import os
# clearing shell
os.system('cls')
print("starting spam")
# waits before spaming
os.system('ping localhost -n 5 > nul')
time.sleep(5)
# reads content from a txt file
f = open("shrek.txt", 'r')
for word in f:
#   enters the script and sends it
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
