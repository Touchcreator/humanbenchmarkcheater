import pyautogui

class ReactionTimeTest:
    @staticmethod
    def run():
        print("test reaction time test")

        while True:
            x, y = pyautogui.position()

            pixel_color = pyautogui.pixel(x, y)

            if pixel_color == (75, 219, 106):
                pyautogui.click()
