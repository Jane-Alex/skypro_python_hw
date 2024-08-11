from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("https://uitestingplayground.com/classattr")
firefox.get("https://uitestingplayground.com/classattr")
sleep(5)

for but in range(3):
    blue_button_chrome = chrome.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button_firefox = firefox.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
   
    blue_button_chrome.click()
    blue_button_firefox.click()
    
    sleep(2)
   
    chrome.switch_to.alert.accept()
    firefox.switch_to.alert.accept()
    