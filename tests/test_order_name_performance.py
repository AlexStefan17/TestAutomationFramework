import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Price import Price
from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login
from selenium.webdriver.support.select import Select


class TestOrderProblem(BaseClass):

    @pytest.fixture(params=LoginData.test_Performance_Login_data)
    def get_data(self, request):
        return request.param

    def test_order(self, get_data):
        log = super().get_logger()
        log_error_messages = []
        prices = Price(self.driver)
        ordered_A_Z = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                        'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
        ordered_Z_A = sorted(ordered_A_Z, reverse=True)
        ordered_price = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]
        ordered_price_reverse = sorted(ordered_price, reverse=True)
        # Login step
        log.info("##### 1. Login step #####")

        login_page = Login(self.driver)
        log.info(f"Username is {get_data['username']}")
        login_page.get_username().send_keys(get_data["username"])
        log.info(f"Password is {get_data['password']}")
        login_page.get_password().send_keys(get_data["password"])
        login_page.login_button().click()
        url = super().get_url()
        assert "https://www.saucedemo.com/inventory.html" == url, "Login failed"
        log.info("Login is pass")

        # Price step
        log.info("##### 2. Order step #####")
        items = prices.get_prices()

        order_menu = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        order_options = order_menu.find_elements(By.TAG_NAME, "option")
        dropdown_list = Select(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))

        for index, item in enumerate(order_options):
            dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
            dropdown.select_by_index(index)

            list_elements = []
            list_prices = []
            for element, i in enumerate(range(len(items))):
                list_elements.append(prices.get_element_name(index))
                price = prices.get_price_element(i)
                list_prices.append(float(price[1::]))

            if index == 0:
                if ordered_A_Z == list_elements:
                    log.info(f"Items name are ordered correctly A-Z order")
                else:
                    error_message = "Order incorrectly A-Z order"
                    log.error(error_message)
                    log_error_messages.append(error_message)
            elif index == 1:
                if ordered_Z_A == list_elements:
                    log.info(f"Items name are ordered correctly Z-A order")
                else:
                    error_message = "Order incorrectly Z-A order"
                    log.error(error_message)
                    log_error_messages.append(error_message)
            elif index == 2:
                if ordered_price == list_prices:
                    log.info(f"Items name are ordered correctly Low to High")
                else:
                    error_message = "Order incorrectly Low to High"
                    log.error(error_message)
                    log_error_messages.append(error_message)
            elif index == 3:
                if ordered_price_reverse == list_prices:
                    log.info(f"Items name are ordered correctly High to Low")
                else:
                    error_message = "Order incorrectly High to Low"
                    log.error(error_message)
                    log_error_messages.append(error_message)

        assert len(log_error_messages) == 0, f"Error log found: {log_error_messages}"