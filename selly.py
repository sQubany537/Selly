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
        background-color: #00BFFF !important; /* DeepSkyBlue */
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

    .coming-soon {
        color: rgba(255, 255, 255, 0.6); text-align: center; font-size: 18px; font-style: italic; margin-top: 10px;
    }

    .proposal-text {
        font-size: 80px; font-weight: bold; color: #1E90FF;
        text-shadow: 0px 0px 30px #00BFFF; text-align: center; margin-top: 50px;
    }

    .quote-text, .tulip-text { color: white; text-align: center; font-size: 22px; font-style: italic; }
    
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
    btn_selly = st.button("Hey Selly")
    btn_love = st.button("I love you")
    btn_sorry = st.button("I want to say sorry :(")
    btn_song = st.button("Our song") # Nowy przycisk
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
    st.markdown("<h1 style='font-size: 80px;'>💙💙💙💙💙</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='heart-message'>
            I can't really express in words what you mean to me. To me you are my world; to me you are my everything. 
            I just want to tell you one thing. I truly love you from my heart and soul. You know what; 
            in my life you play the most important role. I may not tell you every day that you are my life. 
            But, today I want to tell you that I love you lots and lots. My dear if I ever get a chance to 
            choose my next birth, then I would ask God that I wanna be yours again and forever. 
            I love you so much and I mean it.
        </div>
    """, unsafe_allow_html=True)

elif btn_sorry:
    st.snow()
    st.markdown("<h1>I am so sorry...</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sorry-box'>Selly, I really wanted to apologize to you because what I did was terrible... I know it's annoying that I keep apologizing, but I promised myself I wouldn't give up because you're the person I'd do anything for, and that won't change no matter what. Forgive me for my mistake and please give me one last chance, which I don't intend to waste, ever. I love you, my honey... I miss you so much...</div>", unsafe_allow_html=True)

elif btn_song:
    st.markdown("<h1>Mazzy Star - Fade into you 🎶</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='lyrics-box'>
        <b>[Verse 1]</b>
        I wanna hold the hand inside you
        I wanna take the breath that's true
        I look to you and I see nothing
        I look to you to see the truth
        You live your life, you go in shadows
        You'll come apart and you'll go blind
        Some kind of night into your darkness
        Colors your eyes with what's not there

        <b>[Chorus]</b>
        Fade into you
        Strange you never knew
        Fade into you
        I think it's strange you never knew

        <b>[Guitar Solo]</b>

        <b>[Verse 2]</b>
        A stranger light comes on slowly
        A stranger's heart without a home
        You put your hands into your head
        And then its smiles cover your heart

        <b>[Chorus]</b>
        Fade into you
        Strange you never knew
        Fade into you
        I think it's strange you never knew
        Fade into you
        Strange you never knew
        Fade into you
        I think it's strange you never knew

        <b>[Outro]</b>
        I think it's strange you never knew
        </div>
    """, unsafe_allow_html=True)

elif btn_surprise:
    st.markdown("<h1>Meow! 🐾</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg", use_container_width=True)

elif btn_gift:
    st.markdown("<h1>Your Random Gift! 🎁</h1>", unsafe_allow_html=True)
    gifts = [
        {"text": "Free Kisses 💋", "img": "https://cdn.pixabay.com/photo/2016/11/22/19/05/adult-1850073_1280.jpg"},
        {"text": "Free Hugs 🤗", "img": "https://www.placebear.com/800/600.jpg"}, 
        {"text": "Free Cats 🐱", "img": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg"},
        {"text": "Free Chocolate Ice Cream 🍦", "img": "https://cdn.pixabay.com/photo/2016/12/26/16/09/bowl-1932375_1280.jpg"}
    ]
    selected_gift = random.choice(gifts)
    st.markdown(f"<h3>{selected_gift['text']}</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image(selected_gift['img'], use_container_width=True)
    st.balloons()

elif btn_dates:
    st.snow()
    st.markdown("<h1>Our Special Date 🌹</h1>", unsafe_allow_html=True)
    st.markdown("<div class='date-text'>12.03.2025r.</div>", unsafe_allow_html=True)
    st.markdown("<p class='coming-soon'>more dates coming soon...</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; margin-top: 30px;'>Save the date, honey... ✨</h3>", unsafe_allow_html=True)

elif btn_be:
    st.balloons()
    st.markdown("<div class='proposal-text'>Girlfriend?</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <svg width="300" height="300" viewBox="0 0 24 24" fill="#00BFFF" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    <text x="12" y="11" font-family="Arial" font-size="3.5" fill="white" text-anchor="middle" font-weight="bold">LOVE</text>
                </svg>
            </div>
        """, unsafe_allow_html=True)

else:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white; text-align: center;'>Choose something from the menu on the left... 👈</h3>", unsafe_allow_html=True)
