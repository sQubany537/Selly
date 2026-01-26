import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly", layout="wide")

# 2. CSS - Style (Zaktualizowane dla równej długości przycisków)
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #333;
    }

    /* Stylizacja przycisków - teraz wszystkie są równej długości */
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
        
        /* Kluczowe dla równej długości: */
        display: block;
        width: 250px; 
        margin: 10px auto;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px #FF1493;
    }

    h1, h2, h3 {
        color: #FF1493 !important;
        text-align: center;
    }
    
    .sorry-box {
        color: white;
        text-align: center;
        font-size: 20px;
        line-height: 1.8;
        max-width: 700px;
        margin: 40px auto;
        padding: 30px;
        border: 1px solid rgba(255, 20, 147, 0.3);
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.05);
        box-shadow: 0px 0px 20px rgba(255, 20, 147, 0.1);
        font-style: italic;
    }

    .quote-text {
        color: white;
        text-align: center;
        font-size: 22px;
        font-style: italic;
        line-height: 1.6;
        margin: 30px auto;
        max-width: 800px;
    }

    .personal-note {
        color: #AAAAAA;
        text-align: center;
        font-size: 16px;
        font-style: italic;
        margin-top: 40px;
    }

    .tulip-text {
        color: white;
        text-align: center;
        font-size: 24px;
        font-style: italic;
        margin-top: 25px;
    }

    img {
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(255, 20, 147, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. Pasek boczny
with st.sidebar:
    st.markdown("<h2 style='color: white;'>MENU</h2>", unsafe_allow_html=True)
    # Przyciski w sidebarze automatycznie przejmą styl CSS zdefiniowany powyżej
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    btn_sorry = st.button("I want to say sorry :(")
    btn_4 = st.button("Niespodzianka")

# 4. Logika wyświetlania
if btn_selly:
    st.markdown("<h1>Hey my world 🌍💙</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.8, 2, 0.8])
    with col2:
        st.image("https://images.unsplash.com/photo-1520763185298-1b434c919102?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        st.markdown("<p class='tulip-text'>I know how much you love tulips and I want you to be mine tulip</p>", unsafe_allow_html=True)

elif btn_love:
    st.balloons()
    st.markdown("<h1>I love you so much!</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='quote-text'>
            ″ ‘I love you all the way down the lane as far as the river,’ cried Little Nutbrown Hare. <br>
            ‘I love you across the river and over the hills,’ said Big Nutbrown Hare. ”
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>❤️❤️❤️❤️❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p class='personal-note'>My mother used to read me polish version of this book</p>", unsafe_allow_html=True)

elif btn_sorry:
    st.snow()
    st.markdown("<h1>I am so sorry...</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='sorry-box'>
            Selly, I really wanted to apologize to you because what I did was terrible... 
            I know it's annoying that I keep apologizing, but I promised myself I wouldn't give up 
            because you're the person I'd do anything for, and that won't change no matter what. 
            <br><br>
            Forgive me for my mistake and please give me one last chance, which I don't intend to waste, ever. 
            <br><br>
            I love you, my honey... I miss you so much...
        </div>
    """, unsafe_allow_html=True)

elif btn_4:
    st.markdown("<h1>✨ Jesteś wyjątkowa! ✨</h1>", unsafe_allow_html=True)

else:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; text-align: center;'>Wybierz coś z menu po lewej stronie... 👈</h3>", unsafe_allow_html=True)
