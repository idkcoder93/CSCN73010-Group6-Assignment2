# Importing required libs
from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("digit_model.h5")


def preprocess_img(img_path):
    """Preprocesses the input image for prediction.

    Args:
        img_path: The file path of the image to preprocess.

    Returns:
        A numpy array representing the processed image.
    """
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


def predict_result(predict):
    """Predicts the class of the given image array.

    Args:
        predict: A numpy array of the preprocessed image.

    Returns:
        The predicted class label as an integer.
    """
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)
