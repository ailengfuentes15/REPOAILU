import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage


@pytest.fixture(scope="function")
def login_fixture():
   driver = BasePage.initialize_ChromeDriver()
   login_page = LoginPage(driver)
   login_page.login_completo()
   yield driver, login_page
   BasePage(driver).close_browser()

@pytest.fixture(scope="function")
def cart_fixture(login_fixture):
    driver, _ = login_fixture  
    cart_page = CartPage(driver)
    cart_page.cart_completo()
    yield driver, CheckoutPage

   
