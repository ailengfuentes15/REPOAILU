
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage

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
