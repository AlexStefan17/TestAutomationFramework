import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Price import Price
from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login


class TestPrice(BaseClass):

    @pytest.fixture(params=LoginData.test_Performance_Login_data)
    def get_data(self, request):
        return request.param

    def test_price(self, get_data):
        log = super().get_logger()
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

        # Price step
        log.info("##### 2. Price step from items page #####")

        log.info("Calculate total price")
        items = prices.get_prices()
        price_sum = sum(
            [float(item.find_element(By.XPATH, ".//div[@class='inventory_item_price']").text[1:]) for item in items])
        log.info(f"All elements price is {price_sum}")

        log.info("##### 3. Price step from each item page and add to cart #####")
        list_price = []
        price, item_price = None, None
        for item, index in enumerate(range(len(items))):
            try:
                elements = prices.get_prices()
                price = prices.get_price_element(index)
                price = float(price[1::])
                prices.add_to_cart(index)
                element_name = prices.get_element_name(index)
                prices.get_element_link(index)
                item_price = prices.get_element_price_page()
                log.info(f"Element name = {element_name} and price {item_price}")
                log.info(f"Price from main page {price} vs, price on item page {item_price}")
                list_price.append(float(item_price[1::]))
                assert price == float(item_price[1::])
                self.driver.execute_script("window.history.go(-1)")
            except ValueError:
                log.error("Error: Failed to convert price to float")
                self.driver.execute_script("window.history.go(-1)")
            except NoSuchElementException:
                log.error("Error: Element not found")
                self.driver.execute_script("window.history.go(-1)")
            except AssertionError:
                log.error(f"Assertion failed: Expected price {price}, Actual price {float(item_price[1:])}")
                self.driver.execute_script("window.history.go(-1)")
        sum_list_price = sum(list_price)

        try:
            assert price_sum == sum_list_price
            log.info(f"Price sum {price_sum} == sum_list price {sum_list_price}")
        except AssertionError as e:
            log.error(f"Assertion failed: Expected sum {price_sum}, Actual price {sum_list_price}")
            raise e
