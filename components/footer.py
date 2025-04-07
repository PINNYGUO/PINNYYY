import streamlit as st

def display_footer():
    """Display a consistent footer across all pages"""
    footer = """
    <div class="footer">
        <p>© 2023 Sarah Johnson | <a href="mailto:sarah.johnson@example.com" style="color: #2C3E50; text-decoration: none;">Contact</a> | Last updated: May 2023</p>
    </div>
    
    <style>
    .footer {
        margin-top: 30px;
        padding-top: 10px;
        border-top: 1px solid #dee2e6;
        text-align: center;
        font-size: 0.8rem;
        color: #6c757d;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True) 