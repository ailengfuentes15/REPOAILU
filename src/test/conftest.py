import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage

@pytest.fixture(scope="function")
def driver():
    driver = BasePage.initialize_ChromeDriver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_fixture(driver):
    login_page = LoginPage(driver)
    login_page.login_completo()
    return driver, login_page


@pytest.fixture(scope="function")
def cart_fixture(driver):
    cart_page = CartPage(driver)
    cart_page.cart_completo()
    checkout_page = CheckoutPage(driver)
    return driver, checkout_page

