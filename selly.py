import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="Hey Selly App", layout="wide")

# 2. Odrobina CSS, aby wycentrować przycisk w pionie i poziomie
st.markdown("""
    <style>
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; /* Centrowanie w pionie na 80% wysokości ekranu */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Tworzenie kolumn dla centrowania w poziomie
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Wyświetlenie przycisku
    if st.button("Hey Selly"):
        # Akcja po kliknięciu
        st.balloons()
        st.markdown("<h1 style='text-align: center;'>Cześć Selly! ✨</h1>", unsafe_allow_html=True)
