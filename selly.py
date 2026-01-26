import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# 2. CSS - Style
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #333;
    }

    div.stButton > button {
        background-color: #FF1493 !important;
        color: white !important;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #FF1493;
        transition: 0.3s;
        width: 100%;
        margin-bottom: 10px;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px #FF1493;
    }

    h1, h2, h3 {
        color: #FF1493 !important;
        text-align: center;
    }
    
    .tulip-text {
        color: white;
        text-align: center;
        font-size: 24px;
        font-style: italic;
        margin-top: 25px;
        display: block;
    }

    /* Centrowanie obrazka */
    .stImage {
        display: flex;
        justify-content: center;
    }

    img {
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(255, 20, 147, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny z przyciskami
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    # Zmiana nazwy przycisku 3
    btn_sorry = st.button("I want to say sorry :(")
    btn_4 = st.button("Niespodzianka")

# 4. Logika wyświetlania zawartości
if btn_selly:
    # Napis na górze
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    
    # Obrazek pod napisem (wyśrodkowany przez CSS)
    st.image("https://images.unsplash.com/photo-1520763185298-1b434c919102?q=80&w=1000&auto=format&fit=crop", width=600)
    
    # Napis pod obrazkiem
    st.markdown("<p class='tulip-text'>I know how much you love tulips and I want you to be mine tulip</p>", unsafe_allow_html=True)

elif btn_love:
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>❤️❤️❤️❤️❤️</h1>", unsafe_allow_html=True)
    st.toast("Kocham Cię! ❤️")

elif btn_sorry:
    # Zawartość dla przycisku "I want to say sorry :("
    st.markdown("<h1>I want to say sorry :(</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white !important;'>Tutaj możesz dopisać swoje przeprosiny...</h3>", unsafe_allow_html=True)

elif btn_4:
    st.markdown("<h1>✨ Jesteś wyjątkowa! ✨</h1>", unsafe_allow_html=True)

else:
    # Ekran startowy
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Wybierz coś z menu po lewej stronie... 👈</h3>", unsafe_allow_html=True)
