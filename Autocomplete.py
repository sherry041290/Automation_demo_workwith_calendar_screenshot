from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class AutoComplete:

    def test(self):
        base_url = "https://consumer.hottab.us/"
        # snake_case
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)
        # wait
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        # Find the search textbox
        search_text = driver.find_element(By.XPATH, "//div[@id='root']//nav//div[@class='dropdown']/span/span/input[@value='']")
        search_text.send_keys("Sherry")
        suggestion_restaurant = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown show']//a[@href='/sherry-coffee-tea-doi-can']")))
        suggestion_restaurant.click()

        time.sleep(2)
        # driver.quit()


tester = AutoComplete()
tester.test()
