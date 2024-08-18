from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20, 0.1)

driver.get("https://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

txt = wait.until(EC.visibility_of_element_located( (By.CSS_SELECTOR, ".bg-success"))).text
print(txt)

driver.quit()