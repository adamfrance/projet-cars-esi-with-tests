import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app_test import app

def test_list_all_cars_mock():
    """Test the list_all_cars endpoint with mocks"""
    # Create mock collection
    mock_collection = MagicMock()
    mock_collection.count_documents.return_value = 50  # 2 pages
    mock_find = MagicMock()
    mock_find.sort.return_value.skip.return_value.limit.return_value = [
        {"brand": "Test", "make": "Car", "year": 2020, "price": 10000, "km": 5000, "cm3": 1500}
    ]
    mock_collection.find.return_value = mock_find
    
    # Patch app.mongodb
    app.mongodb = {"cars": mock_collection}
    
    # Use test client
    client = TestClient(app)
    response = client.get("/cars/all?page=1")
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert "pages" in data
    assert data["pages"] == 2

def test_list_cars_filtered_by_brand_mock():
    """Test filtering by brand with mocks"""
    # Create mock collection
    mock_collection = MagicMock()
    mock_collection.count_documents.return_value = 25  # 1 page
    mock_find = MagicMock()
    mock_find.sort.return_value.skip.return_value.limit.return_value = [
        {"brand": "Fiat", "make": "Punto", "year": 2020, "price": 10000, "km": 5000, "cm3": 1500}
    ]
    mock_collection.find.return_value = mock_find
    
    # Patch app.mongodb
    app.mongodb = {"cars": mock_collection}
    
    # Use test client
    client = TestClient(app)
    response = client.get("/cars/all?brand=Fiat")
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) > 0

def test_brand_count_mock():
    """Test the brand_count endpoint with mocks"""
    # Create mock collection and aggregate result
    mock_collection = MagicMock()
    mock_agg_result = [{"_id": "Fiat", "count": 10}, {"_id": "Toyota", "count": 5}]
    
    # Make the aggregate method return an iterable
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