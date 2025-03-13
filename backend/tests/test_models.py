import pytest
from pydantic import ValidationError
from models import CarBase

def test_car_base_valid_data():
    # Test with valid data
    data = {
        "brand": "Toyota",
        "make": "Corolla",
        "year": 2020,
        "price": 15000,
        "km": 10000,
        "cm3": 1600
    }
    car = CarBase(**data)
    assert car.brand == "Toyota"
    assert car.make == "Corolla"
    assert car.year == 2020
    assert car.price == 15000
    assert car.km == 10000
    assert car.cm3 == 1600

def test_car_base_invalid_year():
    # Test year validation (should be between 1975 and 2023)
    data = {
        "brand": "Toyota",
        "make": "Corolla",
        "year": 1970,  # Invalid year
        "price": 15000,
        "km": 10000,
        "cm3": 1600
    }
    with pytest.raises(ValidationError):
        CarBase(**data)