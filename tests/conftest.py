import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
            options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = Options()
        firefox_options.add_experimental_option("detach", True)
        # service_obj = Service("/usr/bin/geckodriver")
        # driver = webdriver.Firefox(service=service_obj)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "ie":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
