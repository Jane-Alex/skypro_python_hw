from Lesson7.test_3.ShopPage import Shop
from Lesson7.test_3.CartPage import Cart
from Lesson7.data import *

def test_shop(driver):
    expected_total = "58.29"

    shop = Shop(driver)
    shop.login_form()
    shop.find_items()
    shop.add_items()
    shop.go_cart()

    cart = Cart(driver)
    cart.checkout()
    cart.buyer()
    cart.price()

    assert expected_total in cart.price()

