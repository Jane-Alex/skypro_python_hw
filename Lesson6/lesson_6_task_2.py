from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/textinput")

button = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

button_click = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)

driver.quit()