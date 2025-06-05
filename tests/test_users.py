from fastapi.testclient import TestClient
from app.main import app
import uuid


def test_create_user(db_session, client):
    # Generate a unique ID for this test run
    unique_id = str(uuid.uuid4())
    response = client.post("/users/", json={
        "uid": unique_id,
        "name": "Test User",
        "email": f"test_{unique_id}@example.com",
        "photo_url": "",
        "stack": "Python,FastAPI",
        "experience": 2,
        "modality": "remoto",
        "availability": "inmediata",
        "portfolio": "https://github.com/testuser",
        "is_open_to_offers": True
    })
    assert response.status_code == 200
    assert response.json()["uid"] == unique_id


def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id_or_uid(client):
    # Crear usuario
    client.post("/users/", json={
        "uid": "get_uid_001",
        "name": "Test Get",
        "email": "get@example.com",
        "photo_url": "",
        "stack": "Python",
        "experience": 1,
        "modality": "remoto",
        "availability": "inmediata",
        "portfolio": "https://github.com/testget",
        "is_open_to_offers": True
    })

    # Buscar por ID (asumiendo ID 1 en test db)
    res_by_id = client.get("/users/1")
    assert res_by_id.status_code == 200
    assert res_by_id.json()["uid"] == "get_uid_001"

    # Buscar por UID
    res_by_uid = client.get("/users/get_uid_001")
    assert res_by_uid.status_code == 200
    assert res_by_uid.json()["name"] == "Test Get"
