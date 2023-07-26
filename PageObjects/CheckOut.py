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
    total_price = (By.XPATH, "//div[@class='summary_subtotal_label']")
    tax_price = (By.XPATH, "//div[@class='summary_tax_label']")
    total_price_tax = (By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    finish_button = (By.XPATH, "//button[@id='finish']")
    back_button = (By.XPATH, "//button[@id='back-to-products']")

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

    def get_total_price(self):
        return self.driver.find_element(*CheckOutPage.total_price).text

    def get_tax_price(self):
        return self.driver.find_element(*CheckOutPage.tax_price).text

    def get_total_price_tax(self):
        return self.driver.find_element(*CheckOutPage.total_price_tax).text

    def finish(self):
        return self.driver.find_element(*CheckOutPage.finish_button).click()

    def back_to_products(self):
        return self.driver.find_element(*CheckOutPage.back_button).click()
