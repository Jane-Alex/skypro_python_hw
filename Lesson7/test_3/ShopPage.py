from selenium.webdriver.common.by import By

class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login_form(self):
        self._name = (By.CSS_SELECTOR, "#user-name")
        self._pass = (By.CSS_SELECTOR, "#password")
        self._button = (By.CSS_SELECTOR, "#login-button")
        self.driver.find_element(*self._name).send_keys("standard_user")
        self.driver.find_element(*self._pass).send_keys("secret_sauce")
        self.driver.find_element(*self._button).click()

    def find_items(self):
        self.Backpack = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self. TShirt = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.Onesie = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

    def add_items(self):
        self.driver.find_element(*self.Backpack).click()
        self.driver.find_element(*self.TShirt).click()
        self.driver.find_element(*self.Onesie).click()

    def go_cart(self):
        self.cart = (By.CSS_SELECTOR, "#shopping_cart_container")
        self.driver.find_element(*self.cart).click()
            