import streamlit as st
    import hydralit_components as hc
    import plotly.express as px
    import pandas as pd

    def show_admin_dashboard():
        st.set_page_config(layout="wide")
        
        # Sidebar navigation
        with st.sidebar:
            selected = hc.nav_bar([
                {'icon': "far fa-chart-bar", 'label': "Dashboard"},
                {'icon': "fas fa-users", 'label': "Distributors"},
                {'icon': "fas fa-user-plus", 'label': "Leads"},
                {'icon': "fas fa-envelope", 'label': "Messages"},
                {'icon': "fas fa-cog", 'label': "Settings"}
            ])
        
        if selected == "Dashboard":
            show_admin_metrics()
        elif selected == "Distributors":
            show_distributors_management()
        elif selected == "Leads":
            show_leads_management()
        elif selected == "Messages":
            show_message_templates()
        elif selected == "Settings":
            show_bot_settings()

    def show_admin_metrics():
        # Header with key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = [
            {"label": "Total Distributors", "value": "156", "delta": "+12"},
            {"label": "Active Leads", "value": "1,234", "delta": "+89"},
            {"label": "Conversion Rate", "value": "23%", "delta": "+2.5%"},
            {"label": "Total Revenue", "value": "$12,345", "delta": "+$1,234"}
        ]
        
        for col, metric in zip([col1, col2, col3, col4], metrics):
            with col:
                st.metric(
                    label=metric["label"],
                    value=metric["value"],
                    delta=metric["delta"]
                )
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(create_distributor_growth_chart())
        
        with col2:
            st.plotly_chart(create_leads_conversion_chart())

    def create_distributor_growth_chart():
        # Sample data - replace with real data
        data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=30),
            'Distributors': range(100, 130)
        })
        
        fig = px.line(
            data,
            x='Date',
            y='Distributors',
            title='Distributor Growth Over Time'
        )
        return fig

    def create_leads_conversion_chart():
        # Sample data - replace with real data
        data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=30),
            'Leads': range(100, 130),
            'Converted': range(50, 80)
        })
        
        fig = px.line(
            data,
            x='Date',
            y=['Leads', 'Converted'],
            title='Leads Conversion Over Time'
        )
        return fig

    def show_distributors_management():
        st.header("Distributors Management")
        
        tab1, tab2 = st.tabs(["View Distributors", "Add Distributor"])
        
        with tab1:
            st.dataframe(pd.DataFrame())  # Replace with actual distributor data
            
        with tab2:
            with st.form("add_distributor"):
                arvea_id = st.text_input("Arvea ID")
                telegram_id = st.text_input("Telegram ID")
                opportunity_link = st.text_input("Opportunity Link")
                shop_link = st.text_input("Shop Link")
                submitted = st.form_submit_button("Add Distributor")

    def show_leads_management():
        st.header("Leads Management")
        
        st.dataframe(pd.DataFrame())  # Replace with actual leads data
        
        with st.expander("Lead Details"):
            st.write("Select a lead to view details")

    def show_message_templates():
        st.header("Message Templates")
        
        languages = ["English", "Spanish", "French"]
        selected_language = st.selectbox("Select Language", languages)
        
        template_types = ["Welcome", "Follow-up", "Training"]
        selected_type = st.selectbox("Template Type", template_types)
        
        template_content = st.text_area("Template Content", height=200)
        if st.button("Save Template"):
            st.success("Template saved successfully!")

    def show_bot_settings():
        st.header("Bot Settings")
        
        bot_token = st.text_input("Bot Token", type="password")
        follow_up_days = st.number_input("Follow-up Interval (days)", min_value=1, max_value=10, value=3)
        max_follow_ups = st.number_input("Maximum Follow-ups", min_value=1, max_value=20, value=10)
        
        if st.button("Save Settings"):
            st.success("Settings saved successfully!")
