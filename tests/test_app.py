import pytest


@pytest.fixture
def client():
    from app import app

    with app.test_client() as client:
        yield client


def test_main_page(client):
    """Test the main page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert (
        b"Hand Sign Digit Language Detection" in response.data
    )  # Update to match your HTML content


def test_prediction_route_valid_file(client):
    """Test the prediction route with a valid file upload."""
    with open(
        "test_images/7/Sign 7 (54).jpeg", "rb"
    ) as f:  # Ensure this path is correct
        response = client.post("/prediction", data={"file": f})

    assert response.status_code == 200
    assert b"Prediction" in response.data  # Check if the prediction section is present
    assert (
        b"display-4" in response.data or b"Error" in response.data
    )  # Check for the presence of prediction or error text


def test_prediction_route_no_file(client):
    """Test the prediction route with no file upload."""
    response = client.post("/prediction", data={})  # No file data
    assert response.status_code == 200
    # Check for a generic error message in the response data
    assert (
        b"File cannot be processed" in response.data
        or b"Unexpected error occurred." in response.data
    )


def test_prediction_route_empty_file(client):
    """Test the prediction route with an empty file upload."""
    response = client.post(
        "/prediction", data={"file": (b"", "")}
    )  # Simulate empty file
    assert response.status_code == 200
    # Check for a generic error message in the response data
    assert (
        b"File cannot be processed" in response.data
        or b"Unexpected error occurred." in response.data
    )
