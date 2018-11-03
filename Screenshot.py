from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Screenshot:

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
        login_button = driver.find_element(By.XPATH, "//div[1]/div/div[3]/button[@type='button']")
        login_button.click()
        phone_number_field = driver.find_element(By.XPATH, "//div[@class='login']/div[3]//input[@name='phone']")
        phone_number_field.send_keys("01656940090")
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[2]//div[@role='dialog']/div[@role='document']/div/div//button[@type='button']")))
        submit_button.click()
        validation_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//input[@name='verification_code']")))
        validation_field.send_keys("1234")
        submit_button_final = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[2]//div[@role='dialog']/div[@role='document']//button[@type='button']")))
        submit_button_final.click()
        time.sleep(10)
        screenshot_file_direction = "/Users/DAUAN/Desktop/error.png"
        try:
            driver.save_screenshot(screenshot_file_direction)
            print(" Save the file successfully:: " + screenshot_file_direction)
        except:
            print("Cannot screen shot")

        time.sleep(2)
        # driver.quit()


tester = Screenshot()
tester.test()
