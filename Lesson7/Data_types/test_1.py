from Mainpage import MainPage
from Secondpage import SecondPage
from data import*

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.fill_fields()
    main_page.click_button()

    second_page = SecondPage(chrome_browser)
    second_page.find_fields()
    second_page.get_class_first_name()
    second_page.get_class_last_name()
    second_page.get_class_address()
    second_page.get_class_email()
    second_page.get_class_phone()
    second_page.get_class_zip_code()
    second_page.get_class_city()
    second_page.get_class_country()
    second_page.get_class_job_position()
    second_page.get_class_company()

    assert "success" in second_page.get_class_first_name()
    assert "success" in second_page.get_class_last_name()
    assert "success" in second_page.get_class_address()
    assert "success" in second_page.get_class_email()
    assert "success" in second_page.get_class_phone()
    assert "danger" in second_page.get_class_zip_code()
    assert "success" in second_page.get_class_city()
    assert "success" in second_page.get_class_country()
    assert "success" in second_page.get_class_job_position()
    assert "success" in second_page.get_class_company()
   