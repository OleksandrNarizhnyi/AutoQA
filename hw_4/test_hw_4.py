import time
from selenium.webdriver.common.by import By


def test_button_new_name(driver):
    driver.get("http://uitestingplayground.com/textinput")
    elem_new_button_name = driver.find_element(By.ID, "newButtonName")
    elem_new_button_name.send_keys("ITCH")
    elem_button_set_name = driver.find_element(By.ID, "updatingButton")
    elem_button_set_name.click()
    assert elem_button_set_name.text == "ITCH", "Текст не изменился"

def test_image_upload(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    time.sleep(10)

    elem_div = driver.find_element(By.ID, "image-container")

    elem_img = elem_div.find_elements(By.TAG_NAME, "img")

    assert elem_img[2].get_attribute("alt") == "award"