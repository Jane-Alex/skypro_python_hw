from Lesson7.data import *
from Lesson7.test_2.CalcPage import Calculator

def test_check_calculator(driver):
    calculator = Calculator(driver)
    calculator.set_time()
    calculator.click_buttons()

    assert "15" in calculator.wait_result()
