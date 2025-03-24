from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.set_window_size(700, 400)
# driver.fullscreen_window()

driver.get("https://itcareerhub.de/ru")
# Поиск ссылки "О нас" и клик
about_link = driver.find_element(By.LINK_TEXT, "О нас")
about_link.click()
# Задержка для проверки перехода




# time.sleep(5)
# driver.save_screenshot('./scr/aaa.png')

# driver.refresh()
# time.sleep(2)
# driver.get("https://www.berlin.de/")
# time.sleep(2)
# driver.back() # Возвращаемся на itcareerhub.de/ru
# driver.forward() # Переходим снова на berlin.de

time.sleep(5)
driver.quit()