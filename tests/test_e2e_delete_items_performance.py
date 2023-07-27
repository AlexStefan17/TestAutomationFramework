import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Price import Price
from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login
from PageObjects.CheckOut import CheckOutPage
from selenium.webdriver.support.select import Select


class Teste2eDelete(BaseClass):

    @pytest.fixture(params=LoginData.test_Performance_Login_data)
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

        log.info("##### 4. Click on cart button step #####")
        prices.get_cart_link()
        number_cart_items = prices.get_cart_number()
        if int(number_cart_items) == len(items) // 2:
            log.info(f"Cart number is correctly, expected = {items}, actually = {number_cart_items}")
        else:
            error_message = "Number of items is different"
            log.error(error_message)
            log_error_messages.append(error_message)


        log.info("##### 5. Click on checkout button step #####")
        checkout = CheckOutPage(self.driver)
        checkout.checkout().click()
        checkout.set_first_name().send_keys("Da")
        checkout.set_last_name().send_keys("Da")
        checkout.set_postal_code().send_keys("1234567")
        checkout.click_continue_button().click()

        checkout.get_items()
        list_price = []
        for index, item in enumerate(items[:(len(items) // 2)]):
            item_price = checkout.get_item_price(index)
            list_price.append(float(item_price[1::]))
        total_price = sum(list_price)

        site_price = checkout.get_total_price()
        site_price = site_price[13::]
        if total_price == float(site_price):
            log.info(f"Price is correctly, calculated price = {total_price} = site price {site_price}")
        else:
            error_message = f"Price is incorrectly, calculated price = {total_price} = site price {site_price}"
            log.error(error_message)
            log_error_messages.append(error_message)

        tax_price = checkout.get_tax_price()
        tax_price = tax_price[6::]

        total_price_tax = checkout.get_total_price_tax()
        total_price_tax = total_price_tax[8::]

        price_total_calculated = total_price + float(tax_price)

        if float(total_price_tax) == price_total_calculated:
            log.info(f"Price is correctly, calculated price = {price_total_calculated} = site price {total_price_tax}")
        else:
            error_message = f"Price is incorrectly, calculated price = {price_total_calculated} = site price {total_price_tax}"
            log.error(error_message)
            log_error_messages.append(error_message)

        log.info("##### 6. Click on finish button step #####")
        checkout.finish()
        checkout.back_to_products()
        assert len(log_error_messages) == 0, f"Error log found: {log_error_messages}"