import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="centered")

# 2. CSS dla czarnego tła, różowego przycisku i braku napisów
st.markdown("""
    <style>
    /* Czarne tło */
    .stApp {
        background-color: #000000;
    }

    /* Centrowanie przycisku i obrazka */
    .stButton, .element-container {
        display: flex;
        justify-content: center;
    }

    /* Różowy przycisk */
    div.stButton > button {
        background-color: #FF69B4 !important;
        color: white !important;
        border: none;
        padding: 15px 45px;
        font-size: 26px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #FF69B4;
    }

    /* Ukrycie napisów pod obrazkiem */
    p {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Treść aplikacji
st.write("<br><br>", unsafe_allow_html=True)

# Przycisk
if st.button("Hey Selly"):
    # Efekt lecących serduszek (używamy st.snow, bo technicznie to "opad")
    st.snow() 
    # Dodatkowy efekt wizualny
    st.markdown("<h2 style='text-align: center; color: #FF69B4;'>💖💖💖</h2>", unsafe_allow_html=True)

# Wyraźne niebieskie tulipany
st.image(
    "https://images.unsplash.com/photo-1550159930-40066082a4fc?auto=format&fit=crop&q=80&w=600",
    width=500
)
