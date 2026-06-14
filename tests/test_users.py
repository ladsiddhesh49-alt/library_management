from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Library Management API Running"}


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "John", "email": "john@example.com", "is_librarian": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["is_librarian"] is True


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
