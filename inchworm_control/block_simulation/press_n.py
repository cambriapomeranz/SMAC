import pyautogui
import time

# Enable the fail-safe feature by moving the mouse to the top-left corner
pyautogui.FAILSAFE = True

try:
    while True:
        pyautogui.PAUSE = 0.0
        pyautogui.keyDown('n')  # Press the "n" key down
        pyautogui.keyUp('n')  # Release the "n" key
except KeyboardInterrupt:
    print("Program exited.")
