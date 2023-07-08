from selenium.webdriver.common.by import By

class Price:

    def __init__(self, driver):
        self.driver = driver

    items = (By.XPATH, "//div[@class='inventory_item']")
    price_element = (By.XPATH, ".//div[@class='inventory_item_price']")
    cart_button = (By.XPATH, ".//button[@class='btn btn_primary btn_small btn_inventory']")
    element_name = (By.XPATH, ".//div[@class='inventory_item_name']")
    element_link = (By.XPATH, ".//a[@href='#']")
    price_element_page = (By.XPATH, "//div[@class='inventory_details_price']")
    cart_number = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_link = (By.XPATH, "//a[@class='shopping_cart_link']")

    def get_prices(self):
        return self.driver.find_elements(*Price.items)

    def get_price_element(self, index):
        elements = self.get_prices()
        return elements[index].find_element(*Price.price_element).text

    def add_to_cart(self, index):
        elements = self.get_prices()
        return elements[index].find_element(*Price.cart_button).click()

    def get_element_name(self, index):
        elements = self.get_prices()
        return elements[index].find_element(*Price.element_name).text

    def get_element_link(self, index):
        elements = self.get_prices()
        return elements[index].find_element(*Price.element_link).click()

    def get_element_price_page(self):
        return self.driver.find_element(*Price.price_element_page).text

    def get_cart_number(self):
        return self.driver.find_element(*Price.cart_number).text

    def get_cart_link(self):
        return self.driver.find_element(*Price.cart_link).click()
