from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import*

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def find_fields(self):
        self._first_name = "first-name"
        self._last_name = "last-name"
        self._address = "address"
        self._email = "e-mail"
        self._phone = "phone"
        self._zip_code = "zip-code"
        self._city = "city"
        self._country = "country"
        self._job_position = "job-position"
        self._company = "company"
        self._button = "button"

    def fill_fields(self):
        self.driver.find_element(By.NAME, self._first_name).send_keys("Иван")
        self.driver.find_element(By.NAME, self._last_name).send_keys("Петров")
        self.driver.find_element(By.NAME, self._address).send_keys("Ленина, 55-3")
        self.driver.find_element(By.NAME, self._email).send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, self._phone).send_keys("+7985899998787")
        self.driver.find_element(By.NAME, self._zip_code).send_keys("")
        self.driver.find_element(By.NAME, self._city).send_keys("Москва")
        self.driver.find_element(By.NAME, self._country).send_keys("Россия")
        self.driver.find_element(By.NAME, self._job_position).send_keys("QA")
        self.driver.find_element(By.NAME, self._company).send_keys("SkyPro")

    def click_button(self):
        WebDriverWait(self.driver, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()