import streamlit as st
    import hydralit_components as hc

    def show_landing_page():
        # Configure page
        st.set_page_config(
            page_title="Arvea Elite Bot",
            page_icon="🤖",
            layout="wide"
        )

        # Custom CSS
        st.markdown("""
            <style>
            .main {
                padding: 0rem 1rem;
            }
            .stButton>button {
                width: 100%;
                background-color: #FF4B4B;
                color: white;
                border-radius: 5px;
                height: 3rem;
                font-size: 18px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Hero Section
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
                <h1 style='font-size: 3.5rem;'>
                    Automate Your Arvea Elite Business Growth
                </h1>
                <p style='font-size: 1.5rem; color: #666;'>
                    Transform your network marketing business with our intelligent 
                    Telegram bot and management system
                </p>
            """, unsafe_allow_html=True)
            
            st.button("Get Started")
            
        with col2:
            st.image("static/images/hero-image.png")

        # Features Section
        st.markdown("<h2 style='text-align: center; padding: 2rem 0;'>Key Features</h2>", 
                    unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        features = [
            {
                "icon": "🤖",
                "title": "Automated Lead Generation",
                "description": "24/7 automated lead capture and nurturing through Telegram"
            },
            {
                "icon": "📊",
                "title": "Smart Dashboard",
                "description": "Track your team's performance and leads in real-time"
            },
            {
                "icon": "🌍",
                "title": "Multi-Language Support",
                "description": "Reach prospects worldwide with automated translations"
            }
        ]
        
        for col, feature in zip([col1, col2, col3], features):
            with col:
                st.markdown(f"""
                    <div style='text-align: center; padding: 1rem;'>
                        <h1>{feature['icon']}</h1>
                        <h3>{feature['title']}</h3>
                        <p>{feature['description']}</p>
                    </div>
                """, unsafe_allow_html=True)
