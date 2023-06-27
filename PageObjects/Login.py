from selenium.webdriver.common.by import By

class Login:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    button = (By.XPATH, "//input[@id='login-button']")
    locked_error = (By.CSS_SELECTOR, "h3[data-test='error']")
    def get_username(self):
        return self.driver.find_element(*Login.username)

    def get_password(self):
        return self.driver.find_element(*Login.password)

    def login_button(self):
        return self.driver.find_element(*Login.button)

    def get_locked(self):
        return self.driver.find_element(*Login.locked_error)