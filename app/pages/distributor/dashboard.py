import streamlit as st
    import hydralit_components as hc
    import plotly.express as px
    import pandas as pd

    def show_distributor_dashboard():
        st.set_page_config(layout="wide")
        
        # Sidebar navigation
        with st.sidebar:
            selected = hc.nav_bar([
                {'icon': "far fa-chart-bar", 'label': "My Dashboard"},
                {'icon': "fas fa-user-plus", 'label': "My Leads"},
                {'icon': "fas fa-link", 'label': "My Links"},
                {'icon': "fas fa-graduation-cap", 'label': "Training"},
                {'icon': "fas fa-user-cog", 'label': "Profile"}
            ])
        
        if selected == "My Dashboard":
            show_distributor_metrics()
        elif selected == "My Leads":
            show_my_leads()
        elif selected == "My Links":
            show_my_links()
        elif selected == "Training":
            show_training_materials()
        elif selected == "Profile":
            show_profile_settings()

    def show_distributor_metrics():
        # Personal stats
        st.subheader("My Performance")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("My Leads", "45", "+5")
        with col2:
            st.metric("Team Size", "12", "+2")
        
        # Lead activity chart
        st.plotly_chart(create_lead_activity_chart())
        
        # Recent leads
        st.subheader("Recent Leads")
        show_recent_leads_table()

    def create_lead_activity_chart():
        # Sample data - replace with real data
        data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=30),
            'Leads': [random.randint(1, 10) for _ in range(30)]
        })
        
        fig = px.bar(
            data,
            x='Date',
            y='Leads',
            title='Daily Lead Activity'
        )
        return fig

    def show_my_leads():
        st.header("My Leads")
        st.dataframe(pd.DataFrame())  # Replace with actual leads data

    def show_my_links():
        st.header("My Links")
        st.write("Your opportunity and shop links will be displayed here.")

    def show_training_materials():
        st.header("Training Materials")
        st.write("Training materials will be displayed here.")

    def show_profile_settings():
        st.header("Profile Settings")
        st.write("Your profile settings will be displayed here.")
