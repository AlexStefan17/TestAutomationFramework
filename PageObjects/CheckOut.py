from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.XPATH, "//button[@id='checkout']")
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_button = (By.XPATH, "//input[@id='continue']")
    items = (By.XPATH, "//div[@class='cart_item']")
    item_price = (By.XPATH, ".//div[@class='inventory_item_price']")

    def checkout(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)

    def set_first_name(self):
        return self.driver.find_element(*CheckOutPage.first_name)

    def set_last_name(self):
        return self.driver.find_element(*CheckOutPage.last_name)

    def set_postal_code(self):
        return self.driver.find_element(*CheckOutPage.postal_code)

    def click_continue_button(self):
        return self.driver.find_element(*CheckOutPage.continue_button)

    def get_items(self):
        return self.driver.find_elements(*CheckOutPage.items)

    def get_item_price(self, index):
        items = self.get_items()
        return items[index].find_element(*CheckOutPage.item_price).text