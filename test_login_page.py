from .pages.login_page import LoginPage
import pytest


@pytest.mark.skip(reason="Ожидаем настройку формы")
def test_user_sees_the_elements(browser):
    page = LoginPage(browser, "https://yandex.ru")
    page.open()
    page.click_button_login_page()
    page.should_be_elements_in_login_form()


def test_guest_go_to_registration(browser):
    reg = LoginPage(browser, "https://passport.yandex.by/auth/welcome")
    reg.open()
    reg.click_button_register_new_user()
    reg.should_be_register_form()

