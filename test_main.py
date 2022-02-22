##Functions and tests in the same file

# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app = FastAPI()


# @app.get("/")
# async def read_main():
#     return {"msg": "Hello World"}


# client = TestClient()


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

##Separating tests

# from fastapi.testclient import TestClient

# from .main import app

# client = TestClient(app)


# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
