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

        log.info("##### 3. Click on cart button step #####")
        prices.get_cart_link()
        number_cart_items = prices.get_cart_number()
        if int(number_cart_items) == len(items):
            log.info(f"Cart number is correctly, expected = {items}, actually = {number_cart_items}")
        else:
            error_message = "Number of items is different"
            log.error(error_message)
            log_error_messages.append(error_message)

        self.driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Da")
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Nu")
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("1234567")
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()

        items = self.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        list_price = []
        for item in items:
            item_price = item.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
            list_price.append(float(item_price[1::]))
        total_price = sum(list_price)
        print(total_price)

        site_price = self.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text
        site_price = site_price[13::]
        print(site_price)

        tax_price = self.driver.find_element(By.XPATH, "//div[@class='summary_tax_label']").text
        tax_price = tax_price[6::]
        print(tax_price)

        total_price_tax = self.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").text
        total_price_tax = total_price_tax[8::]
        print(total_price_tax)

        price_total_calculated = total_price + float(tax_price)
        print(price_total_calculated)

        self.driver.find_element(By.XPATH, "//button[@id='finish']").click()
        self.driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()

        assert len(log_error_messages) == 0, f"Error log found: {log_error_messages}"