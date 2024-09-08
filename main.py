import streamlit as st
from languagemodel import answer,RandomFact
from scientificName import get_scientific_name
from classes import get_classes
from randomBird import random_bird
from Predict import predict_image

# Bird labels according to dataset
categories= get_classes()


# Streamlit app layout
def dashboard():
    st.title("Bird STUDIO :baby_chick:")

    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📈 Bird Classifier ", "❓ Q&A", ":star: Random Facts"])
    # Tab1: Bird Classifier Dashboard
    tab1.subheader("Bird Classifier ")
    col1, col2 = tab1.columns(2)
    uploaded_file = col1.file_uploader("Upload a bird photo", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

    if uploaded_file:
        col2.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        is_clicked = col1.button("Classify")
        if is_clicked:
            result = predict_image(uploaded_file)
            col1.metric(label="Bird :", value=result)
            col1.metric(label="Scientific Name :", value=get_scientific_name(result))


    # Add a placeholder for questions and answers
    tab2.subheader("Questions and Answers")
    question = tab2.text_input("Enter your question:")

    if question:
        tab2.write(f"Your question: {question}")
        tab2.write(f"Answer: {answer(question)}")

    # Add a placeholder for questions and answers
    tab3.subheader("Generate a Random Fact about birds")
    random_clicked = tab3.button("Generate")

    if random_clicked:
        img, b_name = random_bird()
        half1, half2 = tab3.columns(2)
        half2.header(b_name)
        half2.write(RandomFact(b_name))
        half1.image(img, width=300)




# Main function to run the dashboard
if __name__ == "__main__":
    dashboard()
    #use streamlit run main.py to run
