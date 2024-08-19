from selenium.webdriver.common.by import By
from data import *

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Maria")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Petrova")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("117115")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label")
    price_total = total.text.strip().replace("Total: $", "")
    last_price_total = "58.29"
    assert price_total == last_price_total


    


