from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

count = 0

chrome.get("http://uitestingplayground.com/dynamicid")
firefox.get("http://uitestingplayground.com/dynamicid")

blue_button_chrome = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
blue_button_firefox = firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

for but in range(3):
    blue_button_chrome = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    blue_button_firefox = firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

    count = count + 1
    sleep(3)
print(count)
