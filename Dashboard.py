import streamlit as st
import tensorflow as tf
import matplotlib.pylab as plab
import numpy as np
from skimage.transform import resize

# Loading the models
model2 = tf.keras.models.load_model('./models/INDIAN_model.h5')
model1 = tf.keras.models.load_model('./models/my_model.h5')

# Bird labels according to dataset
categories1 = ['QUETZAL', 'CANARY', 'CROW', 'PINK ROBIN', 'PEACOCK', 'VIOLET BACKED STARLING', 'PUFFIN',
               'FLAME BOWERBIRD', 'HAWFINCH', 'SNOWY OWL']
categories2 = ['MANGROVE CUCKOO', 'ALEXANDRINE PARAKEET', 'CROW', 'PEACOCK', 'COPPERSMITH BARBET', 'HOUSE SPARROW',
               'TRUMPTER SWAN', 'INDIAN VULTURE', 'INDIAN PITTA', 'INDIAN ROLLER', 'STRIPED OWL']
general_category = ['CUCKOO', 'PARROT', 'CROW', 'PEACOCK', 'BARBET', 'SPARROW', 'SWAN', 'VULTURE', 'PITTA',
                    'ROLLER', 'OWL']

# Function to check the image and predict the bird's name
def check_image(img):
    img = plab.imread(img)
    img = resize(img, (128, 128))
    img_array = img.reshape((1,) + img.shape)

    prediction1 = model1.predict(img_array)
    predicted_class_index1 = tf.argmax(prediction1, axis=1).numpy()[0]
    prediction2 = model2.predict(img_array)
    predicted_class_index2 = tf.argmax(prediction2, axis=1).numpy()[0]

    return categories1[predicted_class_index1], categories2[predicted_class_index2], general_category[predicted_class_index2]

# Streamlit app layout
def dashboard():
    st.title("Bird Classifier :baby_chick:")

    # Tabs for different sections
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

    # Tab 1: Dashboard with Chart
    tab1.subheader("A tab with a chart")
    # Assuming Dashboard is a function you've defined elsewhere
    tab1.Dashboard.dashboard()  # Adjust this line according to your Dashboard function

    # Tab 2: Data display and Q&A section
    tab2.subheader("A tab with the data")
    data = np.random.randn(10, 1)
    tab2.write(data)

    # Bird Classifier Section
    col1, col2 = st.columns(2)

    uploaded_file = col1.file_uploader("Upload a bird photo", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if uploaded_file:
        col2.image(uploaded_file, caption='Uploaded Image', width=300, use_column_width=True)
        is_clicked = col1.button("Classify")

        if is_clicked:
            val1, val2, val3 = check_image(uploaded_file)
            col1.metric(label="Bird (model1):", value=val1)
            col1.metric(label="Bird (model2):", value=val2)
            col1.metric(label="Generalized model:", value=val3)

# Main function to run the dashboard
if __name__ == "__main__":
    dashboard()
