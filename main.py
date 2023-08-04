import streamlit as st
from pathlib import Path


if __name__ == "__main__":

    # --- PATH SETTING ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    resume_file = current_dir / "file" / "nitinchaudhari.pdf"
    css_file = current_dir / "styles" / "main.css"

    # --- GENERAL SETTING ---
    PAGE_TITLE = "Digital CV | Nitin Chaudhari"
    PAGE_ICON = ":boy:"
    NAME = "Nitin Chaudhari"
    DESCRIPTION = """
        Data Engineer, Developer, Part-Time Freelancer.
        """
    EMAIL = "nitinchaudhariofficial@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/nitin-chaudhari/",
        "GitHub": "https://github.com/nitin-chaudhari?tab=repositories",
        "Instagram": "https://www.instagram.com/neeteenchaudhari/",
        "Twitter": "https://twitter.com/chhichhoraaaa"
    }
    PROJECTS = {
        "🏆 Airline Passenger Satisfaction Predictor": "https://github.com/nitin-chaudhari/airline-passenger-satisfaction-predictor",
        "🏆 Online Shoppersc Intention Predictor": "https://github.com/nitin-chaudhari/online-shoppers-intention-predictor",
        "🏆 EDA Fifa Dataset Analysis": "https://github.com/nitin-chaudhari/eda-fifa-dataset",
    }
    
    # --- PAGE CONFIG ---
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
    
    # --- READING FILES ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    # --- NAVIGATION BAR ---
    st.markdown(f"<ul class='nav-bar'><a class='link' href='#summary'>Summary</a>\
                <a class='link' href='#experience'>Experience</a>\
                <a class='link' href='#skills'>Skills</a>\
                <a class='link' href='#projects'>Projects</a>\
                </ul>",unsafe_allow_html=True)

    # --- PROFILE ---
    st.markdown(f"<h1 style='color:rgb(255, 75, 75);'>Hello, I am {NAME}</h1>",unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="pdf",
    )
    st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
    st.markdown("<hr>",unsafe_allow_html=True)
    st.subheader("Links")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- SUMMARY ---
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<h3 id='#summary'>Summary</h3>",unsafe_allow_html=True)
    st.write(
        """
        - ✔️ 1.7 Years expereince developing and maintaining data pipelines.
        - ✔️ Strong hands on experience and knowledge in Python, JavaScript, SQL
        - ✔️ Good understanding of Data Warehouse, Data Modelling, Cloud and Data Science & Machine Learning
        - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        """
        )

    # --- WORK HISTORY ---
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<h3 id='#experience'>Experience</h3>",unsafe_allow_html=True)

    # --- JOB 1
    st.write("🚧", "**Data Engineer | [Blazeclan Technologies Pvt Ltd](https://www.blazeclan.com/india/)**")
    st.write("11/2021 - Present")
    st.write("**Project** - Data Accelerator Tool")
    st.write(
        """
        - ► Developed a data analytics tool for ETL pipeline.
        - ► Implemented dashboards for loaded tables in ETL pipeline.
        - ► Implemented script generator for databases.
        - **:red[Technologies]**: Python, Pandas, SQL.
        """
        )
    
    st.write("**Project** - CSSG Track (Globe Telecom)")
    st.write(
        """
        - ► Migrated python code into javascript code.
        - ► Implemented snowflake stored procedures.
        - ► Implemented airflow dag for scheduling jobs.
        - **:red[Technologies]**: Snowflake, JavaScript, Python, SQL, AWS S3, Apache Airflow 
        """
        )
    
    st.write("**Project** - EDO Track (Globe Telecom)")
    st.write(
        """
        - ► Developed and maintained ELT data pipeline for loading 300+ tables having more than 500+ TB of data.
        - ► Implemented automation tool for reducing daily manual work.
        - ► Implemented Data Quality Framework which can be reused.
        - **:red[Technologies]**: Snowflake, JavaScript, Python, SQL, AWS S3, Apache Airflow 
        """
        )

    # --- SKILLS ---
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<h3 id='#skills'>Skills</h3>",unsafe_allow_html=True)
    st.write(
        """
        - 👩‍💻 Programming: Python (Numpy, Pandas, Scikit-learn,  Streamlit), JavaScript, SQL.
        - 🔂 Framework: Pyspark, Streamlit, Flask(Beginner), Django(Beginner)
        - 📊 Data Visulization: Plotly, Matplotlib, Seaborn.
        - 📚 Modeling: Logistic regression, Linear regression, Decision trees
        - 🗄️ Databases: Postgres, MySQL.
        - 🏭 Data Warehouse: Snowflake.
        - ☁ Cloud: AWS(S3, RDS, Athena, Glue, Glue Workflow)
        """
        )

    # --- PROJECTS ---
    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown("<h3 id='#projects'>Projects</h3>",unsafe_allow_html=True)
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")
