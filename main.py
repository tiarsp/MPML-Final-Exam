import pickle
import streamlit as st

# Membaca model
try:
    with open('resto_model.sav', 'rb') as file:
       resto_model = pickle.load(file)
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan file berada di jalur yang benar.")
except Exception as e:
    st.error(f"Error saat memuat model: {e}")

# Function to validate if the input is an integer
def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to simulate prediction logic
def predict(Menu_Item, Menu_Category, Ingredients, Price):
    # Placeholder logic for prediction
    # You can replace this with actual model prediction logic
    if int(Price) > 50:
        return 1  # success
    else:
        return 0  # failed

# Title of the application
st.title("Prediksi Profitabilitas Menu Restoran")

# Form for user input
with st.form(key='profit_form'):
    Menu_Item = st.text_input("Menu Item")
    Menu_Category = st.text_input("Menu Category")
    Ingredients = st.text_input("Ingredients")
    Price = st.text_input("Price")

    # Submit button for the form
    submit_button = st.form_submit_button(label='Prediksi')

# Validation and prediction logic after form submission
if submit_button:
    if (is_valid_integer(Menu_Item) and is_valid_integer(Menu_Category) and is_valid_integer(Ingredients) and is_valid_integer(Price)):
        
        st.success("All inputs are valid integers.")
        
        # Perform prediction
        prediction = predict(Menu_Item, Menu_Category, Ingredients, Price)
        
        # Display prediction result
        if prediction == 1:
            st.success("Predicted Profit: Success (1)")
        else:
            st.error("Predicted Profit: Failed (0)")
    else:
        st.error("Please enter valid integer values.")