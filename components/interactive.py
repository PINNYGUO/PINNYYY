import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def display_interactive_chart():
    """Display an interactive chart for visualization"""
    st.subheader("Interactive Data Visualization")
    
    # Create sample data
    chart_type = st.selectbox(
        "Select Chart Type", 
        ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
    )
    
    # Generate random data based on user input
    data_points = st.slider("Number of data points", 5, 50, 20)
    
    # Create random data
    np.random.seed(42)  # For reproducibility
    x = np.arange(data_points)
    y = np.random.randn(data_points).cumsum()
    
    # Display the selected chart
    if chart_type == "Line Chart":
        st.line_chart(pd.DataFrame({"values": y}, index=x))
    elif chart_type == "Bar Chart":
        st.bar_chart(pd.DataFrame({"values": y}, index=x))
    elif chart_type == "Area Chart":
        fig, ax = plt.subplots()
        ax.fill_between(x, y)
        st.pyplot(fig)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        st.pyplot(fig)
        
    # Add download capability for the data
    df = pd.DataFrame({"x": x, "y": y})
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="chart_data.csv",
        mime="text/csv",
    ) 