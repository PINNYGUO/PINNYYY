import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Data Science
    **University of XYZ** | *September 2020 - May 2022*
    
    - GPA: 3.9/4.0
    - Thesis: "Applying Machine Learning Techniques to Predict Customer Behavior in E-commerce"
    - Relevant Coursework: Advanced Machine Learning, Deep Learning, Natural Language Processing, Data Visualization, Statistical Methods for Data Science, Big Data Analytics
    
    ### Bachelor of Science in Computer Science
    **ABC University** | *September 2016 - May 2020*
    
    - GPA: 3.7/4.0
    - Graduated with Honors
    - Relevant Coursework: Algorithms and Data Structures, Database Systems, Computer Networks, Operating Systems, Software Engineering, Web Development
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 