import pytest


class TestGetPage:

    def test_get_posts_status(self, get_page):
        """
        Verifica que GET /posts devuelva 200 OK
        """
        response = get_page.get("/posts")
        assert response.status_code == 200

    def test_get_posts_list_structure(self, get_page):
        """
        Verifica que /posts devuelva una lista con elementos
        """
        response = get_page.get("/posts")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list), "La respuesta debe ser una lista"
        assert len(data) > 0, "La lista no debe estar vacía"

    def test_get_first_item_structure(self, get_page):
        """
        Valida la estructura del primer post:
        - Debe ser un dict
        - Debe incluir las claves userId, id, title, body
        - Valida tipos de datos
        """
        response = get_page.get("/posts")
        assert response.status_code == 200
        
        posts = response.json()
        first = posts[0]

        assert isinstance(first, dict), "El item debe ser un diccionario"

        expected_keys = {"userId", "id", "title", "body"}
        assert expected_keys.issubset(first.keys()), "Faltan claves obligatorias"

        assert isinstance(first["userId"], int)
        assert isinstance(first["id"], int)
        assert isinstance(first["title"], str)
        assert isinstance(first["body"], str)

    def test_get_single_post(self, get_page):
        """
        Verifica GET /posts/1 devuelve un post válido
        """
        response = get_page.get("/posts/1")
        assert response.status_code == 200

        post = response.json()
        assert isinstance(post, dict)
        assert post["id"] == 1

    def test_get_with_params(self, get_page):
        """
        Valida que GET con parámetros filtre los resultados
        """
        response = get_page.get("/posts", params={"userId": 1})
        assert response.status_code == 200

        posts = response.json()
        assert len(posts) > 0

        for p in posts:
            assert p["userId"] == 1, "El parámetro userId no filtró correctamente"

    def test_get_invalid_endpoint(self, get_page):
        """
        Verifica comportamiento ante un endpoint inexistente.
        JSONPlaceholder devuelve 404.
        """
        response = get_page.get("/endpoint_que_no_existe")
        
        # response será None si raise_for_status corta el flujo.
        assert response is None or response.status_code == 404
