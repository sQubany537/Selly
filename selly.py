import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="centered")

# 2. CSS dla czarnego tła, różowego przycisku i braku napisów
st.markdown("""
    <style>
    /* Czarne tło całej strony */
    .stApp {
        background-color: #000000;
    }

    /* Centrowanie elementów */
    .stButton, .element-container {
        display: flex;
        justify-content: center;
    }

    /* Stylizacja przycisku - intensywny róż */
    div.stButton > button {
        background-color: #FF1493 !important; /* Deep Pink */
        color: white !important;
        border: none;
        padding: 18px 50px;
        font-size: 28px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 20px #FF1493;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0px 0px 35px #FF1493;
    }

    /* Ukrycie napisów i obramowań pod obrazkiem */
    p, [data-testid="stImageCaption"] {
        display: none !important;
    }
    
    img {
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Treść strony
st.write("<br><br>", unsafe_allow_html=True)

# Przycisk
if st.button("Hey Selly"):
    # Efekt serduszek
    st.toast("💖💖💖💖💖")
    st.snow() # Standardowy efekt opadu (najbliższy sercom w Streamlit)
    st.markdown("<h1 style='text-align: center; color: #FF1493;'>❤️ SELLY ❤️</h1>", unsafe_allow_html=True)

# Zdjęcie niebieskich tulipanów (używamy stabilnego linku do ciemnych tulipanów)
st.image(
    "https://images.unsplash.com/photo-1550159930-40066082a4fc?q=80&w=800&auto=format&fit=crop", 
    width=600
)
