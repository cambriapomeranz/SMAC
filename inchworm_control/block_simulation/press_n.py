import pyautogui
import time

# Enable the fail-safe feature by moving the mouse to the top-left corner
pyautogui.FAILSAFE = True

try:
    while True:
        pyautogui.keyDown('n')  # Press the "n" key down
        time.sleep(0.1)  # hold
        pyautogui.keyUp('n')  # Release the "n" key
        time.sleep(0.1)  # wait
except KeyboardInterrupt:
    print("Program exited.")
