from src.pages.CheckoutPage import CheckoutPage
from selenium.webdriver.common.by import By
import pytest
import time


class TestCheckout:

    @classmethod
    def setup_class(cls): #hace esto primero antes de cualquier otra cosa
        cls.driver = CheckoutPage.initialize_ChromeDriver()
        cls.checkoutPage = CheckoutPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        CheckoutPage(cls.driver).close_browser()


    def test_checkout_complete(self, cart_fixture):
        driver, checkoutPage = cart_fixture

        self.checkoutPage.enter_first_name()
        time.sleep(3)
        self.checkoutPage.enter_last_name()
        self.checkoutPage.enter_postal_code()
        self.checkoutPage.click_continue_button()
        self.checkoutPage.click_finish_button()

        complete_text = checkoutPage.get_text(checkoutPage.complete_order)

        assert "Thank you for your order!" in complete_text
