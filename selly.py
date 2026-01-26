import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="centered")

# 2. Stylizacja CSS (przycisk gradientowy i tło)
st.markdown("""
    <style>
    /* Miłe, białe tło strony */
    .stApp {
        background-color: white;
    }

    /* Stylizacja przycisku Hey Selly */
    div.stButton > button {
        background: linear-gradient(to right, #00BFFF, #FF69B4); /* Niebiesko-różowy */
        color: white;
        border: none;
        padding: 15px 35px;
        font-size: 22px;
        font-weight: bold;
        border-radius: 30px;
        display: block;
        margin: 0 auto; /* Centrowanie przycisku */
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Centrowanie obrazka */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Elementy strony
# Przycisk na górze
if st.button("Hey Selly"):
    st.balloons()

# Obrazek niebieskich tulipanów bezpośrednio pod przyciskiem
st.image(
    "https://img.freepik.com/premium-photo/blue-tulips-field-bright-sunny-day_78361-4682.jpg", 
    width=500
)
