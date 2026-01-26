import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# 2. CSS - Style (Poprawione domykanie bloków)
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
    
    img {
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(255, 20, 147, 0.3);
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    btn_3 = st.button("Niespodzianka 1")
    btn_4 = st.button("Niespodzianka 2")

# 4. Logika wyświetlania
if btn_selly:
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1520763185298-1b434c919102?q=80&w=1000&auto=format&fit=crop", width=600)

elif btn_love:
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>❤️❤️❤️❤️❤️</h1>", unsafe_allow_html=True)
    st.toast("Kocham Cię! ❤️")

elif btn_3:
    st.markdown("<h1>🌸 Piękny dzień, Selly! 🌸</h1>", unsafe_allow_html=True)

elif btn_4:
    st.markdown("<h1>✨ Jesteś wyjątkowa! ✨</h1>", unsafe_allow_html=True)

else:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Wybierz coś z menu po lewej stronie... 👈</h3>", unsafe_allow_html=True)
