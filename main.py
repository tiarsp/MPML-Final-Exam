
import pickle
import streamlit as st

# Fungsi untuk memuat model dari file
def load_model(filename):
    with open(filename, 'rb') as file:
        svm_model = pickle.load(file)
    return svm_model

# Muat model Random Forest yang telah disimpan
model_filename = 'resto_model.sav'
svm_model = load_model(model_filename)

# Fungsi untuk melakukan prediksi dan menentukan kategori profitabilitas
def predict_profitability(features):
    # Melakukan prediksi dengan model
    profitability_prediction = svm_model.predict([features])
    
    # Menentukan kategori profitabilitas berdasarkan prediksi
    if profitability_prediction[0] == 0:
        profitability_category = 'low'
    elif profitability_prediction[0] == 1:
        profitability_category = 'medium'
    else:
        profitability_category = 'high'
    
    return profitability_category

# Judul web
st.title('Prediksi Profitabilitas Menu Restoran')

# Input data dengan contoh angka valid untuk pengujian
menu_item = st.number_input('Menu Item', min_value=0)
menu_category = st.number_input('Menu Category', min_value=0)
ingredients = st.number_input('Ingredients', min_value=0)
price = st.number_input('Price', min_value=0)

# Inisialisasi variabel untuk prediksi
profitability_prediction = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Convert input to appropriate data types
        menu_item = int(menu_item)
        menu_category = int(menu_category)
        ingredients = int(ingredients)
        price = int(price)

        # Melakukan prediksi
        profitability_prediction = predict_profitability([menu_item, menu_category, ingredients, price])

        # Menentukan kategori profitabilitas berdasarkan prediksi
        st.success(f'Profitabilitas: {profitability_prediction}')

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
        