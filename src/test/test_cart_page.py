from src.pages.CartPage import CartPage

class TestCart:

    def test_add_products_cart(self, login_fixture):

        driver, login_page = login_fixture
        cart_page = CartPage(driver)

        cart_page.add_products_cart()

        products_text = cart_page.get_text(cart_page.cart_agregado)

        assert "1" == products_text, f"Se esperaba '1' en el texto, pero se obtuvo: {products_text}"

    def test_navigate_cart(self,login_fixture):

        driver, login_page = login_fixture
        cart_page = CartPage(driver)

        cart_page.add_products_cart()
        cart_page.verify_navigate_cart()

        bag_text = cart_page.get_text(cart_page.bag_cart)

        assert "Sauce Labs Backpack" == bag_text, f"Se esperaba 'Sauce Labs Backpack' en el texto, pero se obtuvo: {bag_text}"
