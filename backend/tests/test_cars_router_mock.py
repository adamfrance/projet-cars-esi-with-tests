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