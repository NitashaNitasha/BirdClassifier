from classes import get_classes
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load categories and the model
categories = get_classes()
model_path = 'models/model.keras'
model = tf.keras.models.load_model(model_path)

# Function to predict the bird's name from an image
def predict_image(img_file):
    # Load and preprocess the image
    img = load_img(img_file, target_size=(224, 224))
    img_array = np.expand_dims(img, axis=0)  # Add batch dimension

    # Predict the class index and confidence
    prediction = model.predict(img_array)
    pred_index = np.argmax(prediction, axis=1)[0]
    pred_confidence = np.max(prediction)

    # Get the predicted bird class name
    pred_class = categories[pred_index]

    # if pred_confidence<0.3:
    #     return "Unable to identify"

    return pred_class


def main():
    print(predict_image('temp.jpeg'))

if __name__=='__main__':
    main()