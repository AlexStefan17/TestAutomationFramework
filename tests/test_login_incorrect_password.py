import pytest
from selenium.webdriver.common.by import By

from TestData.Login import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.Login import Login


class TestLogin(BaseClass):

    @pytest.fixture(params=LoginData.test_incorrect_password_Login_data)
    def get_data(self, request):
        return request.param

    def test_standard_login(self, get_data):
        log = super().get_logger()
        login_page = Login(self.driver)
        log.info(f"Username is {get_data['username']}")
        login_page.get_username().send_keys(get_data["username"])
        log.info(f"Password is {get_data['password']}")
        login_page.get_password().send_keys(get_data["password"])
        login_page.login_button().click()
        error_text = login_page.get_locked().text
        assert "Epic sadface: Username and password do not match any user in this service" == error_text
        log.info("Login is locked")
