import streamlit as st
import time

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="centered")

# 2. CSS dla czarnego tła i różowego przycisku
st.markdown("""
    <style>
    /* Czarne tło całej strony */
    .stApp {
        background-color: #000000;
    }

    /* Centrowanie przycisku i obrazka */
    .stButton, .element-container {
        display: flex;
        justify-content: center;
    }

    /* Stylizacja różowego przycisku */
    div.stButton > button {
        background-color: #FF69B4; /* Intensywny różowy */
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 50px;
        transition: 0.3s;
        box-shadow: 0px 0px 20px rgba(255, 105, 180, 0.5);
    }

    div.stButton > button:hover {
        background-color: #FF1493; /* Ciemniejszy różowy po najechaniu */
        transform: scale(1.1);
        box-shadow: 0px 0px 30px rgba(255, 105, 180, 0.8);
    }

    /* Usunięcie napisu pod obrazkiem */
    .stImage > div > p {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logika serduszek
def heart_snow():
    # Funkcja st.snow() domyślnie wysyła płatki śniegu, 
    # ale możemy "oszukać" system używając st.toast lub efektu wizualnego
    st.snow() # Standardowy efekt opadu (płatki)
    # Dodatkowy efekt napisu z sercami na środku
    st.markdown("<h1 style='text-align: center;'>❤️💖❤️</h1>", unsafe_allow_html=True)

# 4. Zawartość strony
st.write("<br><br>", unsafe_allow_html=True)

# Przycisk
if st.button("Hey Selly"):
    st.snow() # W Streamlit st.snow() to jedyny wbudowany efekt "opadu"
    st.toast("❤️❤️❤️") # Małe serduszka w rogu

# Obrazek niebieskich tulipanów (bez napisu pod spodem)
st.image(
    "https://images.unsplash.com/photo-1550159930-40066082a4fc?q=80&w=1000&auto=format&fit=crop", 
    width=500
)
