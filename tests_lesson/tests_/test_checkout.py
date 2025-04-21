import pytest
from selenium import webdriver

from tests_lesson.pages_.checkout_page import CheckoutPage
from tests_lesson.pages_.inventory_page import InventoryPage
from tests_lesson.pages_.login_page import LoginPage
from tests_lesson.pages_.card_page import CartPage
import time


class TestCheckout:
    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        LoginPage(driver).success_login()
        yield driver
        driver.quit()

    @pytest.fixture(scope='class')
    def inventory_page(self, driver):
        return InventoryPage(driver)


    @pytest.fixture(scope='class')
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture(scope='class')
    def cart_page(self, driver):
        return CartPage(driver)

    @pytest.fixture(scope="class")
    def checkout_page(self, driver):
        return CheckoutPage(driver)

    def test_get_checkout_total_page(self, inventory_page, login_page, cart_page, checkout_page):
        login_page.success_login()
        login_page.accept_alert()
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        cart_page.processed_to_checkout()
        checkout_page.field_checkout_form('jone', 'dou', 2354)
        total_price = checkout_page.get_total_price()
        assert '29.99' in total_price , "Итоговая цена не видна"