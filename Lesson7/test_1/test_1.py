from Lesson7.test_1.MainPage import MainPage
from Lesson7.test_1.SecondPage import SecondPage
from Lesson7.data import*

def test_fill_fields(driver):
    main_page = MainPage(driver)
    main_page.find_fields()
    main_page.fill_fields()
    main_page.click_button()

    secondPage = SecondPage(driver)
    secondPage.find_fields()
    secondPage.get_class_first_name()
    secondPage.get_class_last_name()
    secondPage.get_class_address()
    secondPage.get_class_email()
    secondPage.get_class_phone()
    secondPage.get_class_zip_code()
    secondPage.get_class_city()
    secondPage.get_class_country()
    secondPage.get_class_job_position()
    secondPage.get_class_company()

    assert "success" in secondPage.get_class_first_name()
    assert "success" in secondPage.get_class_last_name()
    assert "success" in secondPage.get_class_address()
    assert "success" in secondPage.get_class_email()
    assert "success" in secondPage.get_class_phone()
    assert "danger" in secondPage.get_class_zip_code()
    assert "success" in secondPage.get_class_city()
    assert "success" in secondPage.get_class_country()
    assert "success" in secondPage.get_class_job_position()
    assert "success" in secondPage.get_class_company()
   