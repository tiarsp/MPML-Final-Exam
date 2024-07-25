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

# Judul web
st.title('Prediksi Profit Menu Restoran')

# Input data dengan contoh angka valid untuk pengujian
Appetizer = st.text_input('Appetizer', '0')
Beverages = st.text_input('Beverages', '1')
Dessert = st.text_input('Dessert', '0')
MainCourse = st.text_input('MainCourse', '0')

harga_menu = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Convert input to appropriate data types
        Appetizer = int(Appetizer)
        Beverages = int(Beverages)
        Dessert = int(Dessert)
        MainCourse = int(MainCourse)

        # Melakukan prediksi
        price_prediction = resto_model.predict([[Appetizer, Beverages,
                                                 Dessert, MainCourse]])

        # Menentukan kategori harga berdasarkan prediksi
        if profit_prediction[0] == 1:
            harga_menu = 'low'
        elif profit_prediction[0] == 2:
            harga_menu = 'medium'
        else:
            harga_menu = 'high'
        
        st.success(harga_menu)

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    