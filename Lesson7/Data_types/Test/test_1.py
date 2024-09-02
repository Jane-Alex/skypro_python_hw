from Data_types.Pages.Mainpage import MainPage
from Data_types.Pages.Datafildes import DataFild

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.filling_in_the_fields()
    main_page.click_submit_button()

    data_fild = DataFild(chrome_browser)
    data_fild.find_fields()

    assert "success" in data_fild.get_class("first_name")
    assert "success" in data_fild.get_class("last_name")
    assert "success" in data_fild.get_class("address")
    assert "success" in data_fild.get_class("email")
    assert "success" in data_fild.get_class("phone")
    assert "danger" in data_fild.get_class("zip_code")
    assert "success" in data_fild.get_class("city")
    assert "success" in data_fild.get_class("country")
    assert "success" in data_fild.get_class("job_position")
    assert "success" in data_fild.get_class("company")