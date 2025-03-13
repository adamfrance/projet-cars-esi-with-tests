import pytest
from fastapi.testclient import TestClient

async def test_list_all_cars(client, mongodb, sample_cars_data):
    # Test the list_all_cars endpoint
    response = client.get("/cars/all?page=1")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert "pages" in data
    assert len(data["results"]) > 0

async def test_list_cars_filtered_by_brand(client, mongodb, sample_cars_data):
    # Test filtering by brand
    brand = "Fiat"  # Use a brand from your sample data
    response = client.get(f"/cars/all?brand={brand}")
    assert response.status_code == 200
    data = response.json()
    for car in data["results"]:
        assert car["brand"] == brand

async def test_brand_count(client, mongodb, sample_cars_data):
    # Test the brand_count endpoint
    response = client.get("/cars/brand/count")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "_id" in data[0]
    assert "count" in data[0]