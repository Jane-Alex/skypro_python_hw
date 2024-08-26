from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *

def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    WebDriverWait(driver, 40, 0.1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()

    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#address").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert "danger" in driver.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#city").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#country").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert "success" in driver.find_element(
        By.CSS_SELECTOR, "#company").get_attribute("class")