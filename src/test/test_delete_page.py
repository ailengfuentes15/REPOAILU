import pytest


class TestDeletePage:

    def test_delete_created_post(self, delete_page, request):
        """
        Recupera el ID creado por POST desde cache de pytest
        y lo elimina usando DELETE.
        """

        # Recuperar id desde cache
        post_id = request.config.cache.get("created_post_id", None)

        assert post_id is not None, "No se encontró un ID en la cache. Ejecutá primero el test de POST."

        print(f"\nID recuperado de cache para borrar: {post_id}")

        # Ejecutar DELETE
        response = delete_page.delete(f"/posts/{post_id}")

        # Validaciones
        assert response is not None, "DELETE devolvió None (error)"
        assert response.status_code in [200, 204], \
            f"Se esperaba 200 o 204, se obtuvo {response.status_code}"

        # JSONPlaceholder devuelve {} en DELETE
        json_body = response.json()
        assert json_body == {}, "Se esperaba un JSON vacío en DELETE"

        print(f"Post {post_id} eliminado correctamente.")
