import pyautogui

def screenCapture():
    im1= pyautogui.screenshot('test.png')
    location = pyautogui.locateCenterOnScreen('example.png', confidence=0.5)
    print(location)
    pyautogui.moveTo(location, duration=1)
    if location != None:
        pyautogui.press('=')

def main():
    while True:
        screenCapture()

main()