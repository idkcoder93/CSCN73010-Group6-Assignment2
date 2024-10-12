# Importing required libraries
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating the Flask app
app = Flask(__name__)

"""
This module provides a Flask application for image prediction.
It includes routes for rendering the home page and processing image uploads.
"""
# Home route
@app.route("/")
def main():
    """Render the home page."""
    return render_template("index.html")


# Prediction route
@app.route("/prediction", methods=["POST"])
def predict_image_file():
    """Process the uploaded image and predict the result."""
    try:
        if request.method == "POST":
            img = preprocess_img(request.files["file"].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))

    except Exception as e:  # Catching a specific exception
        error = f"File cannot be processed: {str(e)}"
        return render_template("result.html", err=error)

    # Ensure that all return paths return an expression
    return render_template("result.html", err="Unexpected error occurred.")


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
