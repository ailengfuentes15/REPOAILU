
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import pytest



class TestLogin:

    @classmethod
    def setup_class(cls): #hace esto primero antes de cualquier otra cosa
        cls.driver = BasePage.initialize_ChromeDriver()
        cls.LoginPage = LoginPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        BasePage(cls.driver).close_browser()


    def test_login(self):
        self.LoginPage.login_completo()

        products_text = self.LoginPage.get_text(self.LoginPage.product_selector)

        assert "Products" in products_text , f"Se esperaba 'Products' en el texto, pero se obtuvo: {products_text}"
        
    @pytest.mark.smoke
       
    def test_login_invalid_username(self):
        self.LoginPage.open_url()
        self.LoginPage.enter_invalid_username()
        self.LoginPage.enter_password()
        self.LoginPage.click_login_button()

        error_message = self.LoginPage.get_text((By.XPATH, "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out')]"))

        assert "Epic sadface: Sorry, this user has been locked out." in error_message, f"Se esperaba el mensaje de usuario bloqueado pero se obtuvo: {error_message}"
