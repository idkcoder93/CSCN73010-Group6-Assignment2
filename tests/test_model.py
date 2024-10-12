import pytest
import numpy as np
from model import preprocess_img, predict_result

# Basic Test Case
def test_preprocess_img():
    # Assuming there's a sample image file for testing
    img_path = "test_images/3/Sign 3 (42).jpeg"  # Replace with a valid test image path
    processed_img = preprocess_img(img_path)

    # Check if the shape of the processed image is correct
    assert processed_img.shape == (1, 224, 224, 3)


def test_predict_result():
    # Mocking a model prediction
    mock_input = np.random.rand(1, 224, 224, 3)  # Random input
    prediction = predict_result(mock_input)

    # Check if the prediction is an integer (class label)
    assert isinstance(prediction, np.int64) or isinstance(prediction, int)


# Advanced Test Case
def test_predict_result_range():
    mock_input = np.random.rand(1, 224, 224, 3)  # Random input
    prediction = predict_result(mock_input)

    # Check if the prediction is within the expected range of classes
    assert 0 <= prediction < 10  # Assuming there are 10 classes
