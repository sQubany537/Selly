import streamlit as st
import random

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# 2. CSS - Style
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333; }

    div.stButton > button {
        background-color: #FF1493 !important;
        color: white !important;
        border: none;
        padding: 15px 10px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #FF1493;
        transition: 0.3s;
        display: block;
        width: 250px; 
        margin: 10px auto;
    }

    div.stButton > button:hover { transform: scale(1.05); box-shadow: 0px 0px 25px #FF1493; }

    h1, h2, h3 { color: #FF1493 !important; text-align: center; }
    
    .sorry-box {
        color: white; text-align: center; font-size: 20px; line-height: 1.8;
        max-width: 700px; margin: 40px auto; padding: 30px;
        border: 1px solid rgba(255, 20, 147, 0.3); border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.05); font-style: italic;
    }

    .quote-text, .tulip-text { color: white; text-align: center; font-size: 22px; font-style: italic; }

    img { border-radius: 15px; box-shadow: 0px 0px 15px rgba(255, 20, 147, 0.3); }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    btn_sorry = st.button("I want to say sorry :(")
    btn_surprise = st.button("Surprise")
    btn_gift = st.button("Random Gift")

# 4. Logika wyświetlania
if btn_selly:
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.8, 2, 0.8])
    with col2:
        st.image("https://images.unsplash.com/photo-1521236194091-030999589d9c?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        st.markdown("<p class='tulip-text'>I know how much you love tulips and I want you to be mine tulip</p>", unsafe_allow_html=True)

elif btn_love:
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("<div class='quote-text'>″ ‘I love you all the way down the lane as far as the river... ”</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>❤️❤️❤️❤️❤️</h1>", unsafe_allow_html=True)

elif btn_sorry:
    st.snow()
    st.markdown("<h1>I am so sorry...</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sorry-box'>Selly, I really wanted to apologize to you... I love you, my honey... I miss you so much...</div>", unsafe_allow_html=True)

elif btn_surprise:
    st.markdown("<h1>Meow! 🐾</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Stabilny link do losowego kotka
        st.image("https://placekitten.com/600/400", use_container_width=True)

elif btn_gift:
    st.markdown("<h1>Your Random Gift! 🎁</h1>", unsafe_allow_html=True)
    
    # Używamy linków, które generują obrazy dynamicznie (bardzo stabilne)
    gifts = [
        {"text": "Free Kisses 💋", "img": "https://images.unsplash.com/photo-1518133910546-b6c2fb7d79e3?auto=format&fit=crop&w=600"},
        {"text": "Free Hugs 🤗", "img": "https://images.unsplash.com/photo-1555435034-9f88dd91444b?auto=format&fit=crop&w=600"},
        {"text": "Free Cats 🐱", "img": "https://placekitten.com/601/401"},
        {"text": "Free Chocolate Ice Cream 🍦", "img": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=600"}
    ]
    
    selected_gift = random.choice(gifts)
    st.markdown(f"<h3>{selected_gift['text']}</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image(selected_gift['img'], use_container_width=True)
    
    # Dodatkowy efekt radości przy losowaniu
    st.confetti()

else:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; text-align: center;'>Choose something from the menu on the left... 👈</h3>", unsafe_allow_html=True)
