from fastapi.testclient import TestClient

from fastapi_course.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/api')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}
