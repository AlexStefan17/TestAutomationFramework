from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    items = (By.XPATH, "//div[@class='cart_item']")
    item_name = (By.XPATH, "//div[@class='inventory_item_name']")
    def get_items(self):
        return self.driver.find_elements(*CartPage.items)

    def get_item_name(self, index):
        items = self.get_items()
        return items[index].find_element(*CartPage.item_name).text