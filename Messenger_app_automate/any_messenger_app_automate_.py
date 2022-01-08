import pyautogui
import time
text = "I love python"
n = 1
while n is not 0:
    time.sleep(3)
    pyautogui.typewrite(text)
    time.sleep(2)
    pyautogui.press('enter')
    n = 0


