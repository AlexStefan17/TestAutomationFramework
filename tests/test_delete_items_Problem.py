import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Price import Price
from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login
from selenium.webdriver.support.select import Select


class TestDelete(BaseClass):

    @pytest.fixture(params=LoginData.test_Problem_Login_data)
    def get_data(self, request):
        return request.param

    def test_delete(self, get_data):
        log = super().get_logger()
        log_error_messages = []
        prices = Price(self.driver)

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

        log.info("##### 2. Add to cart step #####")
        items = prices.get_prices()
        for index, item in enumerate(items):
            prices.add_to_cart(index)
            if (index + 1) == int(prices.get_cart_number()):
                log.info(f"Cart number is correctly, expected = {index}, actually = {prices.get_cart_number()}")
            else:
                error_message = f"Cart number is incorrectly, expected = {index}, actually = {prices.get_cart_number()}"
                log.error(error_message)
                log_error_messages.append(error_message)

        log.info("##### 3. Remove item from cart #####")
        for index, item in enumerate(items[:(len(items) // 2)]):
            all_items = int(prices.get_cart_number())
            prices.remove_from_cart(index)
            all_items -= 1
            if all_items == int(prices.get_cart_number()):
                log.info(f"Cart number is correctly, expected = {index}, actually = {prices.get_cart_number()}")
            else:
                error_message = f"Cart number is incorrectly, expected = {index}, actually = {prices.get_cart_number()}"
                log.error(error_message)
                log_error_messages.append(error_message)
            if index == 2:
                break

        if int(prices.get_cart_number()) == len(items) // 2:
            log.info(f"Number of items from cart is correctly")
        else:
            error_message = f"Cart number is incorrectly"
            log.error(error_message)
            log_error_messages.append(error_message)

        assert len(log_error_messages) == 0, f"Error log found: {log_error_messages}"