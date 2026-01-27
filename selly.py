elif btn_gift:
    st.markdown("<h1>Your Random Gift! 🎁</h1>", unsafe_allow_html=True)
    
    # Wyselekcjonowane, stabilne linki
    gifts = [
        # Free Kisses - Para
        {"text": "Free Kisses 💋", "img": "https://images.unsplash.com/photo-1518133910546-b6c2fb7d79e3?q=80&w=1000&auto=format&fit=crop"},
        # Free Hugs - Przytulający miś (Zmieniony na pewny link)
        {"text": "Free Hugs 🤗", "img": "https://images.unsplash.com/photo-1555435034-9f88dd91444b?q=80&w=1000&auto=format&fit=crop"},
        # Free Cats - Kotek
        {"text": "Free Cats 🐱", "img": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?q=80&w=1000&auto=format&fit=crop"},
        # Free Ice Cream - Lody czekoladowe
        {"text": "Free Chocolate Ice Cream 🍦", "img": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1000&auto=format&fit=crop"}
    ]
    
    selected_gift = random.choice(gifts)
    st.markdown(f"<h3>{selected_gift['text']}</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        # Dodany parametr catch-all, aby wymusić ładowanie
        st.image(selected_gift['img'], use_container_width=True)
    
    st.balloons()
