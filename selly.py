import streamlit as st
import random

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# Inicjalizacja stanu menu
if 'menu_option' not in st.session_state:
    st.session_state.menu_option = "start"

# 2. CSS - Style
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 1px solid #333; }

    div.stButton > button {
        background-color: #00BFFF !important;
        color: white !important;
        border: none;
        padding: 15px 10px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0px 0px 15px #00BFFF;
        transition: 0.3s;
        display: block;
        width: 250px; 
        margin: 10px auto;
    }

    div.stButton > button:hover { transform: scale(1.05); box-shadow: 0px 0px 25px #1E90FF; }

    h1, h2, h3 { color: #00BFFF !important; text-align: center; }
    
    .sorry-box, .lyrics-box {
        color: white; text-align: center; font-size: 18px; line-height: 1.6;
        max-width: 700px; margin: 20px auto; padding: 30px;
        border: 1px solid rgba(0, 191, 255, 0.3); border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.05);
    }
    
    .lyrics-box { font-style: normal; white-space: pre-line; }

    .date-text {
        font-size: 60px; font-weight: bold; color: #FFFFFF;
        text-shadow: 0px 0px 20px #00BFFF; text-align: center; margin-top: 50px;
    }

    .proposal-text {
        font-size: 80px; font-weight: bold; color: #1E90FF;
        text-shadow: 0px 0px 30px #00BFFF; text-align: center; margin-top: 50px;
        margin-bottom: 0px;
    }

    .wife-text {
        font-size: 24px; color: rgba(0, 191, 255, 0.7); text-align: center; 
        font-style: italic; margin-top: -10px; margin-bottom: 20px;
    }

    .heart-message {
        color: white; text-align: center; font-size: 20px; 
        max-width: 800px; margin: 20px auto; line-height: 1.6; 
        font-style: italic;
    }

    img { border-radius: 15px; box-shadow: 0px 0px 15px rgba(0, 191, 255, 0.3); }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    if st.button("Hey Selly"): st.session_state.menu_option = "selly"
    if st.button("I love you"): st.session_state.menu_option = "love"
    if st.button("I want to say sorry :("): st.session_state.menu_option = "sorry"
    if st.button("Our song"): st.session_state.menu_option = "song"
    if st.button("Create your own cat"): st.session_state.menu_option = "cat"
    if st.button("Surprise"): st.session_state.menu_option = "surprise"
    if st.button("Random Gift"): st.session_state.menu_option = "gift"
    if st.button("Special Dates"): st.session_state.menu_option = "dates"
    if st.button("Will you be my..."): st.session_state.menu_option = "be"

# 4. Logika wyświetlania
if st.session_state.menu_option == "selly":
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.8, 2, 0.8])
    with col2:
        st.image("https://images.unsplash.com/photo-1589244159943-460088ed5c92?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        st.markdown("<p style='color: white; text-align: center; font-size: 22px; font-style: italic;'>I know how much you love tulips and I want you to be mine tulip</p>", unsafe_allow_html=True)

elif st.session_state.menu_option == "love":
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>💙💙💙💙💙</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='heart-message'>I can't really express in words what you mean to me... I truly love you from my heart and soul. In my life you play the most important role. I love you so much and I mean it.</div>", unsafe_allow_html=True)

elif st.session_state.menu_option == "sorry":
    st.snow()
    st.markdown("<h1>I am so sorry...</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='sorry-box'>
            Selly, I really wanted to apologize... If I could, I would take back all the things I did to hurt you. 
            But since I can’t, please consider forgiving me. I want us to work on healing our relationship.
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.menu_option == "song":
    st.markdown("<h1>Mazzy Star - Fade into you 🎶</h1>", unsafe_allow_html=True)
    col_v1, col_v2, col_v3 = st.columns([1, 2, 1])
    with col_v2:
        st.video("https://www.youtube.com/watch?v=avv2IIdDnnk")
    st.markdown("<div class='lyrics-box'>I wanna hold the hand inside you...</div>", unsafe_allow_html=True)

elif st.session_state.menu_option == "cat":
    st.markdown("<h1>Design your Selly-Cat 🐱</h1>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns([1, 1])
    with col_c1:
        cat_color = st.color_picker("Body Color", "#00BFFF")
        show_stripes = st.checkbox("Add Stripes?")
        stripe_color = st.color_picker("Stripe Color", "#FFFFFF") if show_stripes else "#000000"

    # SVG Kota z paskami
    stripes_html = ""
    if show_stripes:
        stripes_html = f"""
            <rect x="80" y="135" width="40" height="5" fill="{stripe_color}" />
            <rect x="75" y="145" width="50" height="5" fill="{stripe_color}" />
            <rect x="80" y="155" width="40" height="5" fill="{stripe_color}" />
            <rect x="90" y="50" width="20" height="3" fill="{stripe_color}" />
            <rect x="90" y="58" width="20" height="3" fill="{stripe_color}" />
        """

    cat_svg = f"""
    <div style="text-align: center;">
        <svg width="300" height="300" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <polygon points="50,60 70,20 90,50" fill="{cat_color}" />
            <polygon points="150,60 130,20 110,50" fill="{cat_color}" />
            <circle cx="100" cy="80" r="50" fill="{cat_color}" />
            {stripes_html if show_stripes else ""}
            <circle cx="80" cy="70" r="8" fill="white" />
            <circle cx="120" cy="70" r="8" fill="white" />
            <circle cx="80" cy="70" r="4" fill="black" />
            <circle cx="120" cy="70" r="4" fill="black" />
            <polygon points="100,85 95,95 105,95" fill="pink" />
            <ellipse cx="100" cy="150" rx="60" ry="40" fill="{cat_color}" />
            <path d="M160,150 Q190,120 170,80" stroke="{cat_color}" stroke-width="10" fill="none" stroke-linecap="round" />
        </svg>
    </div>
    """
    st.markdown(cat_svg, unsafe_allow_html=True)

elif st.session_state.menu_option == "surprise":
    st.markdown("<h1>Meow! 🐾</h1>", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg")

elif st.session_state.menu_option == "gift":
    st.markdown("<h1>Your Random Gift! 🎁</h1>", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2016/11/22/19/05/adult-1850073_1280.jpg", width=500)
    st.balloons()

elif st.session_state.menu_option == "dates":
    st.markdown("<h1>Our Special Date 🌹</h1>", unsafe_allow_html=True)
    st.markdown("<div class='date-text'>12.03.2025r.</div>", unsafe_allow_html=True)

elif st.session_state.menu_option == "be":
    st.balloons()
    st.markdown("<div class='proposal-text'>Girlfriend?</div>", unsafe_allow_html=True)
    st.markdown("<div class='wife-text'>and wife later?</div>", unsafe_allow_html=True)

else:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; text-align: center;'>Choose something from the menu on the left... 👈</h3>", unsafe_allow_html=True)
