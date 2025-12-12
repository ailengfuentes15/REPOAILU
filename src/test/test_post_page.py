import pytest


class TestPostPage:

    def test_create_post(self, post_page, request):
        """
        Crea un post, valida estructura y guarda el ID en cache de pytest
        para usarlo luego en DELETE.
        """

        new_post = {
            "title": "Post generado desde test",
            "body": "Texto de prueba",
            "userId": 1
        }

        response = post_page.post(
            "/posts",
            json=new_post,
            headers={"Content-Type": "application/json"}
        )

        # Validación status
        assert response is not None
        assert response.status_code == 201

        created = response.json()

        # Validaciones básicas
        assert isinstance(created, dict)
        assert created["title"] == new_post["title"]
        assert created["body"] == new_post["body"]
        assert created["userId"] == new_post["userId"]

        # JSONPlaceholder always returns an int ID
        assert "id" in created
        assert isinstance(created["id"], int)

        # Guardar ID creado en pytest cache
        request.config.cache.set("created_post_id", created["id"])

        print(f"\nID guardado en cache: {created['id']}")
