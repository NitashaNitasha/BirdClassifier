from classes import get_classes
import numpy as np
import os

categories=get_classes()
base_image_path='birds-dataset/valid/'

def random_bird():
    # Generate a random result from categories list
    result = np.random.randint(0, len(categories))
    # Select random category and image
    random_category = categories[result]
    random_image_path = base_image_path+random_category+'/3.jpg'
    if os.path.exists(random_image_path):
        return random_image_path,categories[result]
    else:
        return None,categories[result]


