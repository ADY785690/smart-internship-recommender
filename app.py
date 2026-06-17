import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Career & Internship Intelligence Platform",
    layout="wide"
)

st.title("🎯 AI Career & Internship Intelligence Platform")

st.markdown(
    "Get internship recommendations, career matches, salary predictions and skill-gap analysis."
)

st.sidebar.header("Student Profile")

cgpa = st.sidebar.slider("CGPA", 0.0, 10.0, 7.5)

python_skill = st.sidebar.slider("Python Skill", 0, 10, 7)
sql_skill = st.sidebar.slider("SQL Skill", 0, 10, 5)
dsa_skill = st.sidebar.slider("DSA Skill", 0, 10, 5)
ml_skill = st.sidebar.slider("Machine Learning Skill", 0, 10, 4)
communication = st.sidebar.slider("Communication Skill", 0, 10, 7)

projects = st.sidebar.number_input(
    "Projects Completed",
    min_value=0,
    value=3
)

internships = st.sidebar.number_input(
    "Internships",
    min_value=0,
    value=1
)

if st.sidebar.button("Generate Report"):

    data_analyst = (
        python_skill * 2
        + sql_skill * 3
        + communication * 2
    )

    ml_engineer = (
        python_skill * 3
        + ml_skill * 3
        + dsa_skill * 2
    )

    software_engineer = (
        dsa_skill * 3
        + python_skill * 2
        + communication
    )

    quant_analyst = (
        python_skill * 2
        + ml_skill * 2
        + cgpa * 3
    )

    scores = {
        "Data Analyst": min(data_analyst, 100),
        "ML Engineer": min(ml_engineer, 100),
        "Software Engineer": min(software_engineer, 100),
        "Quant Analyst": min(quant_analyst, 100)
    }

    best_role = max(scores, key=scores.get)

    readiness = min(
        (
            cgpa * 5
            + python_skill * 3
            + sql_skill * 2
            + projects * 3
            + internships * 5
        ),
        100
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Career Match", best_role)
    col2.metric("Readiness Score", f"{readiness:.0f}/100")

    if readiness >= 80:
        salary = "12-25 LPA"
    elif readiness >= 60:
        salary = "6-12 LPA"
    else:
        salary = "3-6 LPA"

    col3.metric("Expected Salary", salary)

    skill_gap = []

    if sql_skill < 6:
        skill_gap.append("SQL")

    if ml_skill < 6:
        skill_gap.append("Machine Learning")

    if dsa_skill < 6:
        skill_gap.append("DSA")

    col4.metric("Skill Gaps", len(skill_gap))

    st.subheader("📊 Career Match Analysis")

    career_df = pd.DataFrame(
        {
            "Role": list(scores.keys()),
            "Score": list(scores.values())
        }
    )

    st.bar_chart(
        career_df.set_index("Role")
    )

    st.subheader("🎯 Recommended Internship")

    st.success(
        f"Best Match: {best_role} Internship"
    )

    st.subheader("📉 Skill Gap Analysis")

    if skill_gap:
        for skill in skill_gap:
            st.warning(skill)
    else:
        st.success("No Major Skill Gaps Found")

    st.subheader("🛣 Personalized Roadmap")

    roadmap = []

    if sql_skill < 6:
        roadmap.append("Learn SQL")

    if dsa_skill < 6:
        roadmap.append("Practice DSA")

    if ml_skill < 6:
        roadmap.append("Study Machine Learning")

    roadmap.append("Build More Projects")
    roadmap.append("Apply for Internships")

    for i, step in enumerate(roadmap, start=1):
        st.write(f"Week {i}: {step}")

else:
    st.info("Fill details and click Generate Report")
