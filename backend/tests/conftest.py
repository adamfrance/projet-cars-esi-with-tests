import os
import pytest
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from app import app  # Assurez-vous que le nom du fichier est correct

# Configuration de la base de données de test
TEST_MONGO_URL = os.environ.get("TEST_MONGO_URL", "mongodb://localhost:27017")
TEST_DB_NAME = "cars_test_db"

@pytest.fixture
def client():
    """Fixture for the FastAPI TestClient"""
    client = TestClient(app)  # Modifié ici - n'utilise plus le context manager
    yield client

@pytest.fixture(scope="function")
def mongodb():
    """Fixture for a MongoDB client connected to the test database"""
    client = MongoClient(TEST_MONGO_URL)
    db = client[TEST_DB_NAME]
    yield db
    # Clean up after the test
    client.drop_database(TEST_DB_NAME)
    client.close()

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
async def populated_db(mongodb, sample_cars_data):
    """Fixture providing a database populated with sample data"""
    # Insert sample cars
    mongodb.cars.insert_many(sample_cars_data)
    yield mongodb