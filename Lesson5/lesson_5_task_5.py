from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

firefox.get("https://the-internet.herokuapp.com/inputs")
chrome.get("https://the-internet.herokuapp.com/inputs")

input_field_firefox = firefox.find_element(By.TAG_NAME, "input")
input_field_chrome = chrome.find_element(By.TAG_NAME, "input")

input_field_firefox.send_keys("1000")
input_field_chrome.send_keys("1000")
sleep(3)

input_field_firefox.clear()
input_field_chrome.clear()
sleep(2)

input_field_firefox.send_keys("999")
input_field_chrome.send_keys("999")
sleep(2)

