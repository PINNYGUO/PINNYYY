import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Jane_Doe_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Jane Doe")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** jane.doe@example.com
    - **Phone:** (123) 456-7890
    - **LinkedIn:** [linkedin.com/in/janedoe](https://linkedin.com/in/janedoe)
    - **GitHub:** [github.com/janedoe](https://github.com/janedoe)
    - **Address:** 123 Main St, Anytown, USA
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled software engineer with over 5 years of experience in developing scalable web applications. Proven ability to lead teams, manage projects, and improve software performance. Seeking a challenging role to utilize my technical expertise and problem-solving skills.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Software Engineer, TechCorp Inc.**
    - *June 2019 – Present*
    - Developed and maintained web applications using Python and JavaScript.
    - Improved application performance by 30% through code optimization.
    - Led a team of 5 developers, conducting code reviews and mentoring junior engineers.
    - Collaborated with cross-functional teams to define project requirements and deliverables.

    **Junior Software Developer, WebSolutions LLC**
    - *January 2017 – May 2019*
    - Assisted in the development of client-side applications using HTML, CSS, and JavaScript.
    - Participated in agile sprints and contributed to project planning and task estimation.
    - Implemented unit tests and conducted debugging to ensure code quality.
    """)

    st.header("Education")
    st.markdown("""
    **Bachelor of Science in Computer Science**
    - University of Anytown
    - *Graduated: May 2016*
    - GPA: 3.8/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - AWS Certified Solutions Architect
    - Certified Scrum Master
    """)

    st.header("Projects")
    st.markdown("""
    **E-commerce Website**
    - Developed a full-stack e-commerce application using React and Django.
    - Integrated payment gateways and implemented user authentication.

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **Spanish:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Open-source contributions
    - Blogging about technology trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 