from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("https://the-internet.herokuapp.com/entry_ad")
firefox.get("https://the-internet.herokuapp.com/entry_ad")

wait_chrome = WebDriverWait(chrome, 10)
wait_firefox = WebDriverWait(firefox, 10)

modal_window_chrome = wait_chrome.until(EC.visibility_of_element_located({By.CSS_SELECTOR, ".modal"}))
modal_window_firefox = wait_firefox.until(EC.visibility_of_element_located({By.CSS_SELECTOR, ".modal"}))
    
close_button_chrome = wait_chrome.until(EC.element_to_be_clickable({By.CSS_SELECTOR, ".modal-footer"}))
close_button_firefox = wait_firefox.until(EC.element_to_be_clickable({By.CSS_SELECTOR, ".modal-footer"}))

close_button_chrome.click()
close_button_firefox.click()
time.sleep(5)
