from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def field_checkout_form(self,first_name,last_name, post_code):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        last_name_input = self.driver.find_element(By.ID, "last-name")
        post_code_input = self.driver.find_element(By.ID, "postal-code")
        first_name_input.clear()
        first_name_input.send_keys(first_name)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        post_code_input.clear()
        post_code_input.send_keys(post_code)
        btn = self.driver.find_element(By.ID, "continue")
        btn.click()

    def get_total_price(self):
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total.text