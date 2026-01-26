import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="wide")

# 2. Customowy CSS dla wyglądu
st.markdown("""
    <style>
    /* Miłe, jasne tło strony */
    .stApp {
        background-color: #fdfeff;
    }

    /* Stylizacja przycisku (niebiesko-różowy gradient) */
    .stButton>button {
        background-image: linear-gradient(to right, #00BFFF, #FF69B4);
        color: white;
        font-size: 24px;
        font-weight: bold;
        padding: 15px 50px;
        border-radius: 50px;
        border: none;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        display: block;
        margin: 0 auto;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.2);
    }

    /* Styl dla tekstu pod przyciskiem */
    .custom-text {
        text-align: center;
        font-family: 'Arial', sans-serif;
        color: #4A90E2;
        font-size: 32px;
        margin-top: 30px;
        font-weight: bold;
    }

    /* Centrowanie obrazka */
    .stImage {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Układ strony
# Puste miejsce na górze, żeby wszystko było na środku
st.write("<br><br><br>", unsafe_allow_html=True)

# Przycisk Hey Selly
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Hey Selly"):
        st.balloons()

    # Napis pod przyciskiem
    st.markdown('<p class="custom-text">Hey my world</p>', unsafe_allow_html=True)

    # Niebieskie tulipany (obrazek z sieci)
    st.image("https://img.freepik.com/premium-photo/beautiful-blue-tulips-background_1102497-20054.jpg", 
             caption="Twoje niebieskie tulipany 🌷", 
             use_container_width=True)
