import streamlit as st

st.title("🎯 Smart Internship Recommender")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)

python_skill = st.slider("Python Skill", 0, 10, 5)

ml_skill = st.slider("Machine Learning Skill", 0, 10, 5)

dsa_skill = st.slider("DSA Skill", 0, 10, 5)

finance_interest = st.slider("Finance Interest", 0, 10, 5)

if st.button("Get Recommendation"):

    if ml_skill >= 7 and python_skill >= 7:
        st.success("Recommended Role: ML Engineer")
        st.write("Missing Skills:")
        st.write("- Deep Learning")
        st.write("- MLOps")
        st.write("- Docker")

    elif finance_interest >= 7 and python_skill >= 6:
        st.success("Recommended Role: Quant Analyst")
        st.write("Missing Skills:")
        st.write("- Statistics")
        st.write("- Time Series Analysis")
        st.write("- Options Pricing")

    elif python_skill >= 6:
        st.success("Recommended Role: Data Analyst")
        st.write("Missing Skills:")
        st.write("- SQL")
        st.write("- Power BI")
        st.write("- Excel")

    elif dsa_skill >= 7:
        st.success("Recommended Role: Software Engineer")
        st.write("Missing Skills:")
        st.write("- System Design")
        st.write("- Backend Development")

    else:
        st.warning("Improve your core skills first.")
