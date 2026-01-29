import streamlit as st
import random

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# Inicjalizacja stanu dla wiadomości pod sercami
if 'love_messages' not in st.session_state:
    st.session_state.love_messages = [None] * 5

# 2. CSS - Style
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333; }

    /* Główne przyciski w menu - Ujednolicenie wielkości */
    div.stButton > button {
        background-color: #00BFFF !important;
        color: white !important;
        border: none;
        padding: 10px 5px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #00BFFF;
        transition: 0.3s;
        display: block;
        width: 100% !important; /* Szerokość na cały sidebar */
        min-height: 60px !important; /* Stała wysokość dla każdego przycisku */
        margin: 5px 0px;
    }

    div.stButton > button:hover { transform: scale(1.02); box-shadow: 0px 0px 25px #1E90FF; }

    /* Styl dla przycisków-serduszek w sekcji I Love You */
    .heart-btn > div > button {
        background-color: transparent !important;
        box-shadow: none !important;
        font-size: 50px !important;
        width: auto !important;
        min-height: auto !important; /* Reset wysokości dla serc */
        border: none !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    .heart-btn > div > button:hover {
        transform: scale(1.2);
        background-color: transparent !important;
    }

    h1, h2, h3 { color: #00BFFF !important; text-align: center; }
    
    .sorry-box {
        color: white; text-align: center; font-size: 20px; line-height: 1.8;
        max-width: 700px; margin: 40px auto; padding: 30px;
        border: 1px solid rgba(0, 191, 255, 0.3); border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.05); font-style: italic;
    }

    .date-text {
        font-size: 60px; font-weight: bold; color: #FFFFFF;
        text-shadow: 0px 0px 20px #00BFFF; text-align: center; margin-top: 50px;
    }

    .coming-soon {
        color: rgba(255, 255, 255, 0.6); text-align: center; font-size: 18px; font-style: italic; margin-top: 10px;
    }

    .proposal-text {
        font-size: 80px; font-weight: bold; color: #1E90FF;
        text-shadow: 0px 0px 30px #00BFFF; text-align: center; margin-top: 50px;
    }

    .quote-text, .tulip-text { color: white; text-align: center; font-size: 22px; font-style: italic; margin-bottom: 20px; }

    .heart-msg {
        color: white; text-align: center; font-weight: bold; font-size: 14px;
        animation: fadeIn 1s;
    }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    img { border-radius: 15px; box-shadow: 0px 0px 15px rgba(0, 191, 255, 0.3); }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    # Przyciski menu
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    btn_sorry = st.button("I want to say sorry :(")
    btn_surprise = st.button("Surprise")
    btn_gift = st.button("Random Gift")
    btn_dates = st.button("Special Dates")
    btn_be = st.button("Will you be my...")

# 4. Logika wyświetlania
if btn_selly:
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.8, 2, 0.8])
    with col2:
        st.image("https://images.unsplash.com/photo-1589244159943-460088ed5c92?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        st.markdown("<p class='tulip-text'>I know how much you love tulips and I want you to be mine tulip</p>", unsafe_allow_html=True)

elif btn_love:
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("<div class='quote-text'>″ ‘I love you all the way down the lane as far as the river... ”</div>", unsafe_allow_html=True)
    
    messages = ["My everything 🌍", "My sunshine ☀️", "My soulmate ♾️", "My happiness ✨", "My forever 💙"]
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown('<div class="heart-btn">', unsafe_allow_html=True)
            if st.button("💙", key=f"h_{i}"):
                st.session_state.love_messages[i] = messages[i]
            st.markdown('</div>', unsafe_allow_html=True)
            if st.session_state.love_messages[i]:
                st.markdown(f"<p class='heart-msg'>{st.session_state.love_messages[i]}</p>", unsafe_allow_html=True)

elif btn_sorry:
    st.snow()
    st.markdown("<h1>I am so sorry...</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sorry-box'>Selly, I really wanted to apologize to you because what I did was terrible... I know it's annoying that I keep apologizing, but I promised myself I wouldn't give up because you're the person I'd do anything for, and that won't change no matter what. Forgive me for my mistake and please give me one last chance, which I don't intend to waste, ever. I love you, my honey... I miss you so much...</div>", unsafe_allow_html=True)

elif btn_surprise:
    st.markdown("<h1>Meow! 🐾</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("
