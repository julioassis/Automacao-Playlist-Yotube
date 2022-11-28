import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

pyperclip.copy("https://www.youtube.com/playlist?list=PL5yzrLGzl3FJ3QatJrdr67gXQboKcYKF2")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=415, y=331)

#time.sleep(10)
#print(pyautogui.position())
