# from selenium.webdriver.common.by import By
# import time
#
#
# def test_logo_ich(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310155")
#     assert element, "тест не прошел"
#
#
# def test_link_program(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'Программы')
#     assert element, "тест не прошел"
#
#
# def test_link_pay(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
#     assert element, "тест не прошел"
#
#
# def test_link_news(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'Новости')
#     assert element, "тест не прошел"
#
#
# def test_link_about_us(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'О нас')
#     assert element, "тест не прошел"
#
#
# def test_link_reviews(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'Отзывы')
#     assert element, "тест не прошел"
#
#
# def test_link_lang_ru(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'ru')
#     assert element, "тест не прошел"
#
#
# def test_link_lang_de(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.LINK_TEXT, 'de')
#     assert element, "тест не прошел"
#
#
# def test_click_phone_icon_and_check_text(driver):
#     driver.get("https://itcareerhub.de/ru")
#     element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310161")
#
#     assert element, "Элемент трубка не найден"
#
#     element.click()
#     time.sleep(1)
#     element1 = driver.find_element(By.XPATH, '//*[text()="Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"]')
#
#     assert element1, "Элемент 'Если не дозвонились' - не найден"
