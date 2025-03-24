import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")
    try:
        payment_methods_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
        payment_methods_link.click()
        time.sleep(3)
        payment_methods_link.screenshot("payment_methods_section.png")
        print("Скриншот секции 'Способы оплаты' сохранён как 'payment_methods_section.png'")
    except Exception as e:
        pytest.fail(f"Не удалось найти секцию или сделать скриншот: {e}")