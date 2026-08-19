from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage :
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_input = (By.CSS_SELECTOR, "[data-testid='input-box'][name='id']")             # 실제 사이트의 ID필요
        self.password_input = (By.CSS_SELECTOR, "[data-testid='input-box'][name='password']")       # 실제 사이트의 ID 필요
        self.login_button = (By.CSS_SELECTOR, "form button[type='submit']")     # 실제 사이트의 ID 필요
    
    def enter_username(self, username):
        el = self.wait.until(EC.presence_of_element_located(self.username_input))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.wait.until(EC.presence_of_element_located(self.password_input))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        el = self.wait.until(EC.element_to_be_clickable(self.login_button))
        el.click()

    # 3동작 한번에 처리
    def do_login(self, username, password):
        time.sleep(2) 
        self.enter_username(username)
        time.sleep(0.5) 
        self.enter_password(password)
        time.sleep(0.5)
        self.click_login()
