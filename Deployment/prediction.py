import streamlit as st
import numpy as np
# from keras.models import load_model
from PIL import Image
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Load the GRU model
# model = load_model('model_gru_2')

def run():

    image = Image.open('ecentrix.png')
    st.image(image, caption = 'eCentrix Solutions')
    
    with st.form('Text Message Classification'):
        # Field Input Text
        input_text = st.text_area('Input Text Message', '', help='Enter the text for sentiment prediction')
        
        # Create a submit button
        submitted = st.form_submit_button('Predict')

    # Inference
    if submitted:
        # Make a prediction using the model
        # Convert the input text to lowercase (optional)
        input_text = input_text.lower()

        # Make a prediction using the model
        predictions = model.predict(np.array([input_text]))

        # Map predicted class to labels
        predicted_class = np.argmax(predictions[0])
        class_labels = {0: 'Not Spam', 1: 'Spam'}
        predicted_label = class_labels[predicted_class]

        # Display the results
        st.write('## Text Message Prediction:')
        st.write('Input Text:', input_text)
        st.write('Predicted Class:', predicted_class)
        st.write('Predicted Label:', predicted_label)

if __name__ == '__main__':
    run()
