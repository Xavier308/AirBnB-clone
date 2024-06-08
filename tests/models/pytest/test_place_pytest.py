import pytest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

@pytest.fixture
def host():
    return User("host@example.com", "password123", "Host", "Last")

@pytest.fixture
def place(host):
    return Place(
        name="Beautiful Retreat",
        description="A quiet, cozy spot perfect for weekends.",
        address="123 Country Road",
        city="Hillsboro",
        host=host,
        rooms=3,
        price_per_night=150,
        max_guests=4
    )

@pytest.fixture
def amenity():
    return Amenity("Wi-Fi", "Global")

@pytest.fixture
def review(host, place):
    return Review(host, place, "Loved it!", 5)

def test_place_creation(place):
    assert place.name == "Beautiful Retreat"
    assert place.rooms == 3

def test_add_amenity(place, amenity):
    place.add_amenity(amenity)
    assert amenity in place.amenities

def test_add_review(place, review):
    place.add_review(review)
    assert review in place.reviews
