from selenium.webdriver.common.by import By


class CartPage:

    def _init_(self, driver):
        self.driver = driver

    items = (By.XPATH, "//div[@class='cart_item']")
    item_name = (By.XPATH, "//div[@class='inventory_item_name']")
    remove_button = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")

    def get_items(self):
        return self.driver.find_elements(*CartPage.items)

    def get_item_name(self, index):
        items = self.get_items()
        return items[index].find_element(*CartPage.item_name).text

    def remove_item(self, index):
        items = self.get_items()
        return items[index].find_element(*CartPage.remove_button).click()