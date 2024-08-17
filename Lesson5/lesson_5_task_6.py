from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

firefox.get("https://the-internet.herokuapp.com/login")
chrome.get("https://the-internet.herokuapp.com/login")

name_firefox = firefox.find_element(
    By.ID, "username").send_keys("tomsmith")
name_chrome = chrome.find_element(
    By.ID, "username").send_keys("tomsmith")
sleep(2)

pass_firefox = firefox.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
pass_chrome = chrome.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)

button_firefox = firefox.find_element(By.TAG_NAME, "button").click()
button_chrome = chrome.find_element(By.TAG_NAME, "button").click()
sleep(2)