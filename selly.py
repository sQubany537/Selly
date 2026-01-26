import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# 2. CSS - Style (Czarny motyw + Różowe przyciski + Ukrycie zbędnych elementów)
st.markdown("""
    <style>
    /* Czarne tło całej aplikacji */
    .stApp {
        background-color: #000000;
    }
    
    /* Czarne tło paska bocznego (sidebar) */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #333;
    }

    /* Stylizacja przycisków - intensywny róż */
    div.stButton > button {
        background-color: #FF1493 !important; /* Deep Pink */
        color: white !important;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #FF1493;
        transition: 0.3s;
        width: 100%; /* Przyciski na całą szerokość paska */
        margin-bottom: 10px;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px #FF1493;
    }

    /* Ukrycie napisów i obramowań pod obrazkiem */
    p, [data-testid="stImageCaption"] {
        color: white; /* Tekst domyślnie biały */
    }
     
    /* Styl dla nagłówków */
    h1, h2, h3 {
        color: #FF1493 !important;
        text-align: center;
    }
    
    img {
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(255, 20, 147, 0.3);
        display: block;
        margin-left
