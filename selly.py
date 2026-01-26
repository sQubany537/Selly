import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="centered")

# 2. Stylizacja CSS dla idealnego wyglądu
st.markdown("""
    <style>
    /* Białe tło strony */
    .stApp {
        background-color: #FFFFFF;
    }

    /* Wyśrodkowanie przycisku i obrazka */
    .element-container, .stButton {
        display: flex;
        justify-content: center;
    }

    /* Stylizacja przycisku (niebiesko-różowy gradient) */
    div.stButton > button {
        background: linear-gradient(to right, #00BFFF, #FF69B4);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 50px;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    }

    /* Stylizacja obrazka */
    img {
        border-radius: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Treść aplikacji
# Odstęp od góry
st.write("<br><br>", unsafe_allow_html=True)

# Przycisk
if st.button("Hey Selly"):
    st.balloons()

# Obrazek niebieskich tulipanów
# Używamy stabilnego linku do zdjęcia niebieskich tulipanów
st.image(
    "https://images.unsplash.com/photo-1550159930-40066082a4fc?q=80&w=1000&auto=format&fit=crop", 
    caption="Twoje niebieskie tulipany 🌷",
    width=500
)
