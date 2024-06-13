import pytest
from unittest.mock import MagicMock
from app.models.review import Review
from app.models.user import User
from app.models.place import Place
from app.services.review_service import ReviewService
from app.persistence.data_manager import DataManager

@pytest.fixture
def mock_data_manager():
    mock = MagicMock(spec=DataManager)
    mock.get = MagicMock()
    mock.save = MagicMock()
    mock.update = MagicMock()
    mock.delete = MagicMock()
    mock.get_all_by_user_id = MagicMock()
    mock.get_all_by_place_id = MagicMock()
    return mock

@pytest.fixture
def review_service(mock_data_manager):
    return ReviewService(data_manager=mock_data_manager)

# Test data setup with all required arguments
@pytest.fixture
def user():
    return User(email="user@example.com", password="secure123", first_name="John", last_name="Doe")

@pytest.fixture
def place():
    return Place(
        name="Beautiful Place",
        description="A nice place to visit.",
        address="123 Main St",
        city_id="city123",
        latitude=34.0522,
        longitude=-118.2437,
        host_id="host123",
        rooms=3,
        bathrooms=2,
        price_per_night=150,
        max_guests=4,
        amenities=["WiFi", "Air Conditioning"]
    )


@pytest.fixture
def review(user, place):
    return Review(user=user, place=place, text="Great place, enjoyed our stay!", rating=5)

# Example test for creating a review
def test_create_review_success(review_service, mock_data_manager, user, place):
    mock_data_manager.get.side_effect = [user, place]  # User and Place exist
    review_text = "Great place, enjoyed our stay!"
    review_rating = 5
    expected_review = Review(user=user, place=place, text=review_text, rating=review_rating)

    mock_data_manager.save.return_value = expected_review
    result = review_service.create_review(place.place_id, user.user_id, review_rating, review_text)

    assert result == expected_review
    # assert result.rating == review_rating
    mock_data_manager.save.assert_called_once_with(expected_review)

# Additional tests **

# Test updating a review successfully
def test_update_review_success(review_service, mock_data_manager, review):
    updated_text = "Updated review text."
    updated_rating = 4
    mock_data_manager.get.return_value = review
    review_service.update_review(review.review_id, updated_rating, updated_text)

    assert review.text == updated_text
    assert review.rating == updated_rating
    mock_data_manager.update.assert_called_once_with(review)

# Test updating a review that does not exist
def test_update_review_not_found(review_service, mock_data_manager):
    mock_data_manager.get.return_value = None
    with pytest.raises(ValueError, match="Review not found."):
        review_service.update_review("nonexistent_review_id", 3, "Some text.")

# Test deleting a review successfully
def test_delete_review_success(review_service, mock_data_manager, review):
    mock_data_manager.get.return_value = review
    review_service.delete_review(review.review_id)

    mock_data_manager.delete.assert_called_once_with(review.review_id, Review)

# Test trying to delete a review that does not exist
def test_delete_review_not_found(review_service, mock_data_manager):
    mock_data_manager.get.return_value = None
    with pytest.raises(ValueError, match="Review not found."):
        review_service.delete_review("nonexistent_review_id")

# Test retrieving a review successfully
def test_get_review_success(review_service, mock_data_manager, review):
    mock_data_manager.get.return_value = review
    result = review_service.get_review(review.review_id)

    assert result == review

# Test trying to get a review that does not exist
def test_get_review_not_found(review_service, mock_data_manager):
    mock_data_manager.get.return_value = None
    with pytest.raises(ValueError, match="Review not found."):
        review_service.get_review("nonexistent_review_id")

# Test retrieving all reviews by a user
def test_get_reviews_by_user(review_service, mock_data_manager, review):
    mock_data_manager.get_all_by_user_id.return_value = [review]
    result = review_service.get_reviews_by_user(review.user.user_id)

    assert result == [review]

# Test retrieving all reviews for a place
def test_get_reviews_by_place(review_service, mock_data_manager, review):
    mock_data_manager.get_all_by_place_id.return_value = [review]
    result = review_service.get_reviews_by_place(review.place.place_id)

    assert result == [review]
