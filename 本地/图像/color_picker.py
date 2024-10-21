import pyautogui

def pick_color():
    x, y = pyautogui.position()
    return pyautogui.screenshot().getpixel((x, y))