/# dashboard library
import streamlit as st
# ml library
import tensorflow as tf
import matplotlib.pylab as plab
from skimage.transform import resize

import numpy as np
import pandas as pd

# loading the model
my_model = tf.keras.models.load_model('E:/app devlopment/BirdClassifier/models/my_model.h5')


#  bird labels according to dataset
categories=['QUETZAL','CANARY','CROW','PINK ROBIN','PEACOCK','VIOLET BACKED STARLING','PUFFIN','FLAME BOWERBIRD','HAWFINCH','SNOWY OWL']



def check_image(img):
    '''

    :param img: image file
    :return: predicted bird's name
    '''
    # Read and preprocess the image
    img = plab.imread(img)
    img = resize(img, (128, 128))
    img_array = img.reshape((1,) + img.shape)

    # Make predictions
    prediction = my_model.predict(img_array)
    predicted_class_index = tf.argmax(prediction, axis=1).numpy()[0]
    return categories[predicted_class_index]





# main document
st.title("Bird Classifier :baby_chick:")
col1,col2 =st.columns(2)


# file uploader
uploaded_file = col1.file_uploader("Upload a bird photo", type=["png", "jpg", "jpeg"], accept_multiple_files=False)




# if file is uploaded
if uploaded_file:

    # Display the uploaded image
    col2.image(uploaded_file, caption='Uploaded Image',width=300, use_column_width=True)
    is_clicked=col1.button("Classify")

    # if classify button is clicked
    if is_clicked:

        col1.metric(label="This Bird is classified as:", value=check_image(uploaded_file))
