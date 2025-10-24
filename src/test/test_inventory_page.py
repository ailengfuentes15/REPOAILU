
from src.pages.InventoryPage import InventoryPage

class TestInventory:

    def test_inventory(self, login_fixture):


        driver, login_page = login_fixture
        inventory_page = InventoryPage(driver)

        # Assert de elementos presentes
        assert inventory_page.is_element_present(inventory_page.menu_burger), "Menu burger no está presente"
        assert inventory_page.is_element_present(inventory_page.filter_selector), "Filtro no está presente"
        assert inventory_page.is_element_present(inventory_page.cart_selector), "Carrito no está presente"

        # Assert de elementos visibles
        assert inventory_page.is_element_visible(inventory_page.bag_selector), "Bolso no está visible"
        assert inventory_page.is_element_visible(inventory_page.bike_selector), "Bicicleta no está visible"



