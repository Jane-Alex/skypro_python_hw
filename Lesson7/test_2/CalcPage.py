from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *

class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_time(self):
        field_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        field_input.clear()
        field_input.send_keys(45)

    def click_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self.driver.find_element(By.XPATH, "//span[text() = '=']").click()

    def wait_result(self):
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen" ), "15"))
        return self.driver.find_element(By.CLASS_NAME, "screen").text
