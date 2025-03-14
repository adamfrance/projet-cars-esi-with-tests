import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

def test_list_all_cars_mock():
    """Test the list_all_cars endpoint with mocks instead of real MongoDB integration"""
    from app import app
    
    # Create mock collection
    mock_collection = MagicMock()
    mock_collection.count_documents.return_value = 50  # 2 pages
    mock_collection.find.return_value.sort.return_value.skip.return_value.limit.return_value = [
        {"brand": "Test", "make": "Car", "year": 2020, "price": 10000, "km": 5000, "cm3": 1500}
    ]
    
    # Patch app.mongodb
    app.mongodb = {"cars": mock_collection}
    
    # Use test client
    client = TestClient(app)
    response = client.get("/cars/all?page=1")
    
    # Assertions
    assert response.status_code == 200
    assert "results" in response.json()
    assert "pages" in response.json()

def test_list_cars_filtered_by_brand_mock():
    """Test filtering by brand with mocks"""
    from app import app
    
    # Create mock collection
    mock_collection = MagicMock()
    mock_collection.count_documents.return_value = 25  # 1 page
    mock_collection.find.return_value.sort.return_value.skip.return_value.limit.return_value = [
        {"brand": "Fiat", "make": "Punto", "year": 2020, "price": 10000, "km": 5000, "cm3": 1500}
    ]
    
    # Patch app.mongodb
    app.mongodb = {"cars": mock_collection}
    
    # Use test client
    client = TestClient(app)
    response = client.get("/cars/all?brand=Fiat")
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) > 0
    for car in data["results"]:
        assert car["brand"] == "Fiat"

def test_brand_count_mock():
    """Test the brand_count endpoint with mocks"""
    from app import app
    
    # Create mock collection and aggregate result
    mock_collection = MagicMock()
    mock_agg_result = [{"_id": "Fiat", "count": 10}, {"_id": "Toyota", "count": 5}]
    
    # Make the aggregate method return an iterable that can be converted to a list
    mock_collection.aggregate.return_value = mock_agg_result
    
    # Patch app.mongodb
    app.mongodb = {"cars": mock_collection}
    
    # Use test client
    client = TestClient(app)
    response = client.get("/cars/brand/count")
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "_id" in data[0]
    assert "count" in data[0]