from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Calendar:

    def test(self):
        base_url = "https://www.expedia.com"
        # snake_case
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        driver.find_element(By.ID, "tab-flight-tab-hp").click()

        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "flight-departing-hp-flight")))
        element.click()

        date_to_select = driver.find_element(By.XPATH, "//div[@id='flight-departing-wrapper-hp-flight']/div[@class='datepicker-dropdown']/div/div[2]/table[@class='datepicker-cal-weeks']/tbody/tr[5]/td[4]/button[@type='button']")
        date_to_select.click()
        time.sleep(2)
        driver.quit()


tester = Calendar()
tester.test()
