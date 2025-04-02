from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time



driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/cats.html')
element = driver.find_element(By.XPATH, "//*[@id='bullet']")
el_button = element.parent.find_element(By.XPATH, '//button[text()="View"]')
el_button.click()
time.sleep(3)
assert element


try:
 element = driver.find_element(By.ID, "login-button")
 print("Элемент найден")
except NoSuchElementException:
 print("Элемент не найден")

# element2 = driver.find_element(By.XPATH, '//button[text()="View"]')
# time.sleep(2)
# element2.click()
# time.sleep(3)
# assert element