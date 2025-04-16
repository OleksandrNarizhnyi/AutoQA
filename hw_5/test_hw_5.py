import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_1(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    obj_iframe = driver.find_element(By.ID, 'my-iframe')

    driver.switch_to.frame(obj_iframe)

    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    expected_text = "semper posuere integer et senectus justo curabitur."
    found = any(expected_text in p.text for p in paragraphs)
    assert found, "Текст не найден в iframe"

    # obj_text = driver.find_element(By.XPATH,'//*[contains(normalize-space(text()), "semper posuere integer et senectus justo curabitur.")]')
    # assert obj_text.is_displayed()


def test_2(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 2)
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.="Соглашаюсь"]')))
    accept_cookies_button.click()

    obj_iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    driver.switch_to.frame(obj_iframe)

    photo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-draggable-handle')))
    trash = driver.find_element(By.ID, 'trash')

    action = ActionChains(driver)
    action.drag_and_drop(photo, trash).perform()

    time.sleep(2)

    photos_in_gallery = driver.find_element(By.ID, "gallery")
    photos_in_gallery_li = photos_in_gallery.find_elements(By.TAG_NAME, "li")

    assert len(photos_in_gallery_li) == 3, "Не удалось переместить объект"

    photos_in_trash = driver.find_element(By.ID, 'trash')
    photos_in_trash_li = photos_in_trash.find_elements(By.TAG_NAME, "li")

    assert len(photos_in_trash_li) == 1, "В корзине нет объектов"

