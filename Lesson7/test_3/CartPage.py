from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.check = (By.CSS_SELECTOR, "#checkout")
        self.driver.find_element(*self.check).click()

    def buyer(self):
        self.first_name = (By.CSS_SELECTOR, "#first-name")
        self.driver.find_element(*self.first_name).send_keys("Maria")
        self.last_name = (By.CSS_SELECTOR, "#last-name")
        self.driver.find_element(*self.last_name).send_keys("Petrova")
        self.postcode = (By.CSS_SELECTOR, "#postal-code")
        self.driver.find_element(*self.postcode).send_keys("117115")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.driver.find_element(*self.continue_button).click()

    def price(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total = total_price.text.strip().replace("Total: $", "")
        return total