import pyautogui
import os.path
import time

class AimTrainerTest:
    @staticmethod
    def run():
        target_path = os.path.join("img", "target.png")

        print("Starting in 6 seconds...")
        time.sleep(6)
        while True:

            try:
                x, y = pyautogui.locateCenterOnScreen(target_path, confidence=0.44)


                pyautogui.click(x, y)
            except pyautogui.ImageNotFoundException:
                pass
