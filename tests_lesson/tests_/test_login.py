# import pytest
# from selenium import webdriver
# from tests_lesson.pages_.login_page import LoginPage
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")
#     yield driver
#     driver.quit()
#
# def test_successful_login(driver):
#     login_page = LoginPage(driver)
#     login_page.success_login()
#     assert "inventory.html" in driver.current_url, "Не удалось войти в систему."
#
# def test_invalid_password(driver):
#     """
#     описание теста по шагам
#     :param driver:
#     :return:
#     """
#     login_page = LoginPage(driver)
#     login_page.enter_username("standard_user")
#     login_page.enter_password("wrong_password")
#     login_page.click_on_login_button()
#     error_msg = login_page.get_error_msg
#     assert "Epic sadface: Username and password do not match any user in this service" in error_msg.text, "Test не прошел"
#
# def test_locked_out_user(driver):
#     login_page = LoginPage(driver)
#     login_page.enter_username("locked_out_user")
#     login_page.enter_password("secret_sauce")
#     login_page.click_on_login_button()
#     error_msg = login_page.get_error_msg
#     assert "Sorry, this user has been locked out." in error_msg.text, "Неверное сообщение об ошибке."
#
# def test_empty_username(driver):
#     login_page = LoginPage(driver)
#     login_page.enter_password("secret_sauce")
#     login_page.click_on_login_button()
#     error_msg = login_page.get_error_msg
#     assert "Username is required" in error_msg.text, "Неверное сообщение об ошибке."
#
# def test_empty_password(driver):
#     login_page = LoginPage(driver)
#     login_page.enter_username("standard_user")
#     login_page.click_on_login_button()
#     error_msg = login_page.get_error_msg
#     assert "Password is required" in error_msg.text, "Неверное сообщение об ошибке."
