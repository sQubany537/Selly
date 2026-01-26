import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="wide")

# 2. Customowy CSS do stylizacji strony i przycisku
st.markdown("""
    <style>
    /* Styl dla tła całej strony */
    body {
        background-color: #f0f2f6; /* Bardzo jasny szary/niebieski, delikatny */
    }
    .stApp {
        background-color: #f0f2f6; /* Upewnij się, że główny kontener Streamlit też ma to tło */
    }

    /* Styl dla przycisku */
    .stButton>button {
        background-image: linear-gradient(to right, #00BFFF, #FF69B4); /* Niebiesko-różowy gradient */
        color: white; /* Biały tekst na przycisku */
        font-size: 2em; /* Większa czcionka */
        padding: 20px 40px; /* Większy rozmiar przycisku */
        border-radius: 12px; /* Zaokrąglone rogi */
        border: none; /* Bez ramki */
        cursor: pointer;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); /* Delikatny cień */
        transition: all 0.2s ease-in-out; /* Płynne przejścia */
    }
    .stButton>button:hover {
        transform: scale(1.05); /* Lekkie powiększenie po najechaniu */
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Większy cień po najechaniu */
    }

    /* Centrowanie kontenera przycisku w pionie i poziomie */
    html, body, .stApp {
        height: 100%;
        margin: 0;
        padding: 0;
    }
    .stApp > header {
        display: none; /* Ukryj domyślny nagłówek Streamlit */
    }
    .main .block-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: calc(100vh - 5rem); /* Wysokość, uwzględniając padding */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Tworzenie kolumn dla centrowania w poziomie
# Używamy tylko jednej kolumny, bo całe centrowanie załatwimy CSS-em dla .block-container
col1, = st.columns([1]) # Pozostawiamy dla struktury, choć główną robotę robi CSS

with col1:
    # Wyświetlenie przycisku
    # streamlit.button() domyślnie jest wewnątrz kontenera st.columns,
    # który jest centrowany przez nasz CSS.
    if st.button("Hey Selly"):
        # Akcja po kliknięciu
        st.balloons()
        st.markdown("<h1 style='text-align: center; color: #555;'>Cześć Selly! ✨</h1>", unsafe_allow_html=True)
