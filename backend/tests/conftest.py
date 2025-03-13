import os
import pytest
from fastapi.testclient import TestClient
import mongomock
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    """Fixture for the FastAPI TestClient"""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def mock_mongodb():
    """Fixture providing a mock MongoDB client"""
    client = mongomock.MongoClient()
    db = client["cars_test_db"]
    # Create the cars collection
    db.create_collection("cars")
    return db

@pytest.fixture
def sample_cars_data():
    """Fixture providing sample car data for tests"""
    return [
        {
            "brand": "Fiat",
            "make": "Punto",
            "year": 2018,
            "price": 12000,
            "km": 45000,
            "cm3": 1400
        },
        {
            "brand": "Toyota",
            "make": "Corolla",
            "year": 2019,
            "price": 18000,
            "km": 30000,
            "cm3": 1600
        },
        # Add more sample cars as needed
    ]

@pytest.fixture
def populated_mock_db(mock_mongodb, sample_cars_data):
    """Fixture providing a mock database populated with sample data"""
    # Insert sample cars
    mock_mongodb.cars.insert_many(sample_cars_data)
    
    # Set up the app to use our mock database
    app.mongodb = mock_mongodb
    
    yield mock_mongodb