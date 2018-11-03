from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class JavaScript:

    def test(self):
        base_url = "https://consumer.hottab.us/"
        # snake_case
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)

        # window height & width
        window_height = driver.execute_script(" return window.innerHeight; ")
        window_width = driver.execute_script(" return window.innerWidth; ")
        print(" Height: " + str(window_height))
        print(" Width: " + str(window_width))
        time.sleep(2)

        driver.execute_script("return window.")
        driver.quit()


tester = JavaScript()
tester.test()
