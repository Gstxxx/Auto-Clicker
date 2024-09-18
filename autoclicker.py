import pyautogui
import keyboard
import threading

def autoclicker(interval=0.01):
    clicking = False
    print("Autoclicker ready. Press '-' to start, '+' to stop.")
    
    def click_thread():
        nonlocal clicking
        while True:
            if clicking:
                pyautogui.click()
                pyautogui.PAUSE = interval
            else:
                pyautogui.PAUSE = 0.1

    threading.Thread(target=click_thread, daemon=True).start()

    while True:
        if keyboard.is_pressed('-') and not clicking:
            clicking = True
            print("Autoclicker started.")
        elif keyboard.is_pressed('+') and clicking:
            clicking = False
            print("Autoclicker stopped.")

if __name__ == "__main__":
    autoclicker()