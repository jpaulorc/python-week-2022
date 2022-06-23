from fastapi.testclient import TestClient

from beerlog.api import api

client = TestClient(api)


def test_add_beer_api():
    response = client.post(
        "/beers",
        json={
            "name": "Skol",
            "style": "KornPilsner",
            "flavor": 1,
            "image": 1,
            "cost": 3,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Skol"
    assert result["id"] == 1
