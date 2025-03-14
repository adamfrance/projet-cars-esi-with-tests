import pytest
from fastapi.testclient import TestClient
import mongomock
from app_test import app  # Import the test app

@pytest.fixture
def client():
    """Fixture for the FastAPI TestClient"""
    return TestClient(app)

@pytest.fixture
def mock_mongodb():
    """Fixture providing a mock MongoDB client"""
    # Create and return a mock database
    return app.mongodb

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
        }
    ]

@pytest.fixture
def populated_mock_db(mock_mongodb, sample_cars_data):
    """Fixture providing a mock database populated with sample data"""
    # Clear existing data
    mock_mongodb.cars.delete_many({})
    
    # Insert sample cars
    mock_mongodb.cars.insert_many(sample_cars_data)
    
    yield mock_mongodb
    
    # Clean up
    mock_mongodb.cars.delete_many({})