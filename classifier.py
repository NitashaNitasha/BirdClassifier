import tensorflow as tf
import matplotlib.pylab as plab
from skimage.transform import resize
# ml library
import numpy as np
import pandas as pd

# loading the model
my_model = tf.keras.models.load_model('E:/app devlopment/BirdClassifier/my_model.h5')


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



