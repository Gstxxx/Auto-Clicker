import pyautogui
import time
import keyboard

def autoclicker(interval=0.001):
    clicking = False
    print("Autoclicker ready. Press '-' to start, '+' to stop.")
    
    while True:
        if keyboard.is_pressed('-') and not clicking:
            clicking = True
            print("Autoclicker started.")
        elif keyboard.is_pressed('+') and clicking:
            clicking = False
            print("Autoclicker stopped.")
        
        if clicking:
            pyautogui.click()
            time.sleep(interval)

if __name__ == "__main__":
    autoclicker()