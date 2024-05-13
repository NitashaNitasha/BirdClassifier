# dashboard library
import streamlit as st

import classifier


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

        col1.metric(label="This Bird is classified as:", value=classifier.check_image(uploaded_file))
