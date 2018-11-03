from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ScrollToView:

    def test(self):
        base_url = "https://consumer.hottab.us/"
        # snake_case
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)

        # Scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)

        # Scroll up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)

        # Scroll the element into view
        element = driver.find_element(By.CSS_SELECTOR, ".navbar-brand-wrapper [alt]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        # driver.execute_script("window.scrollBy(0,-150);")

        # Native way to Scroll the element into view
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("Location is: " + str(location))
        time.sleep(5)
        # driver.quit()


tester = ScrollToView()
tester.test()
