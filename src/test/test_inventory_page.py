
import pytest
from src.pages.InventoryPage import InventoryPage

class TestInventory:

    @pytest.mark.parametrize(
        "element, mensaje",
        [
            ("menu_burger", "Menu burger no está presente"),
            ("filter_selector", "Filtro no está presente"),
            ("cart_selector", "Carrito no está presente"),
        ]
    )
    def test_elementos_presentes(self, login_fixture, element, mensaje):
        driver, login_page = login_fixture
        inventory_page = InventoryPage(driver)

        locator = getattr(inventory_page, element)
        assert inventory_page.is_element_present(locator), mensaje

    @pytest.mark.parametrize(
        "element, mensaje",
        [
            ("bag_selector", "Bolso no está visible"),
            ("bike_selector", "Bicicleta no está visible"),
        ]
    )
    def test_elementos_visibles(self, login_fixture, element, mensaje):
        driver, login_page = login_fixture
        inventory_page = InventoryPage(driver)

        locator = getattr(inventory_page, element)
        assert inventory_page.is_element_visible(locator), mensaje


