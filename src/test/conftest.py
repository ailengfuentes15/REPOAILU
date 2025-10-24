import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage


@pytest.fixture(scope="function")
def login_fixture():
   driver = BasePage.initialize_ChromeDriver()
   login_page = LoginPage(driver)
   login_page.login_completo()
   yield login_page
   BasePage(driver).close_browser()
