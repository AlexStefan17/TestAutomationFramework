import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verify_Xpath_presence(self, time, text):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.XPATH, text)))

    def get_url(self):
        url = self.driver.current_url
        return url

