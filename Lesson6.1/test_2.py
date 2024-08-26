from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    field_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    field_input.clear()
    field_input.send_keys(45)

    driver.find_element(By.XPATH, "//span[text() = '7']").click()
    driver.find_element(By.XPATH, "//span[text() = '+']").click()
    driver.find_element(By.XPATH, "//span[text() = '8']").click()
    driver.find_element(By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "screen" ), "15"))

    result = driver.find_element(By.CLASS_NAME, "screen").text

    assert result == "15"
