import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Price import Price
from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login
from selenium.webdriver.support.select import Select


class TestOrderStandard(BaseClass):

    @pytest.fixture(params=LoginData.test_StandardLogin_data)
    def get_data(self, request):
        return request.param

    def test_order(self, get_data):
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

        log.info("##### 2. Click on cart button step #####")
        prices.get_cart_link()
        number_cart_items = prices.get_cart_number()
        if int(number_cart_items) == len(items):
            log.info(f"Cart number is correctly, expected = {items}, actually = {number_cart_items}")
        else:
            error_message = "Number of items is different"
            log.error(error_message)
            log_error_messages.append(error_message)

        assert len(log_error_messages) == 0, f"Error log found: {log_error_messages}"