import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By


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

    def test_url_valida(self):
        self.LoginPage.login_completo()

        current_url = self.LoginPage.login_data["url"]


        assert "https://www.saucedemo.com/inventory.html" == current_url


    #def test_login_fixture(login_fixture): #aca uso al fixture como precondicion, por ende hace todo el login, debo usarlo a futuro
        #login_page = login_fixture

