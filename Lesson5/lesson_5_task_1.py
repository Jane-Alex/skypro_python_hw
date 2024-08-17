from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

for but in range(5):
    add_button = chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    add_button = firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    
    chrome_delete_buttons = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
    firefox_delete_buttons = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')

print(f"Chrome - размер списка: {len(chrome_delete_buttons)}")

print(f"Firefox - размер списка: {len(firefox_delete_buttons)}")


