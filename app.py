import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Career & Internship Intelligence Platform",
    layout="wide"
)

st.title("🎯 AI Career & Internship Intelligence Platform")
st.markdown(
    "Get internship recommendations, career matches, salary predictions, company suggestions and skill-gap analysis."
)

# SIDEBAR
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
        python_skill * 2 +
        sql_skill * 3 +
        communication * 2
    )

    ml_engineer = (
        python_skill * 3 +
        ml_skill * 3 +
        dsa_skill * 2
    )

    software_engineer = (
        dsa_skill * 3 +
        python_skill * 2 +
        communication
    )

    quant_analyst = (
        python_skill * 2 +
        ml_skill * 2 +
        cgpa * 3
    )

    scores = {
        "Data Analyst": data_analyst,
        "ML Engineer": ml_engineer,
        "Software Engineer": software_engineer,
        "Quant Analyst": quant_analyst
    }

    total = sum(scores.values())

    percentages = {
        role: round((score / total) * 100, 1)
        for role, score in scores.items()
    }

    best_role = max(percentages, key=percentages.get)

    readiness = min(
        (
            cgpa * 5 +
            python_skill * 3 +
            sql_skill * 2 +
            projects * 3 +
            internships * 5
        ),
        100
    )

    resume_score = min(
        (
            projects * 8 +
            internships * 15 +
            cgpa * 5 +
            python_skill * 2
        ),
        100
    )

    if readiness >= 80:
        salary = "12-25 LPA"
    elif readiness >= 60:
        salary = "6-12 LPA"
    else:
        salary = "3-6 LPA"

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Career Match", best_role)
    col2.metric("Readiness Score", f"{readiness:.0f}/100")
    col3.metric("Resume Score", f"{resume_score:.0f}/100")
    col4.metric("Expected Salary", salary)

    st.divider()

    st.subheader("📊 Career Match Percentage")

    match_df = pd.DataFrame({
        "Role": list(percentages.keys()),
        "Match %": list(percentages.values())
    })

    st.bar_chart(
        match_df.set_index("Role")
    )

    st.subheader("🎯 Recommended Internship")

    st.success(
        f"Best Internship Match: {best_role}"
    )

    company_map = {
        "Data Analyst": [
            "Deloitte",
            "EY",
            "KPMG",
            "Fractal Analytics"
        ],
        "ML Engineer": [
            "TCS AI",
            "Tiger Analytics",
            "NVIDIA",
            "Google"
        ],
        "Software Engineer": [
            "Amazon",
            "Microsoft",
            "Flipkart",
            "Adobe"
        ],
        "Quant Analyst": [
            "Jane Street",
            "Tower Research",
            "WorldQuant",
            "Quadeye"
        ]
    }

    st.subheader("🏢 Recommended Companies")

    for company in company_map[best_role]:
        st.write("✅", company)

    st.divider()

    st.subheader("📉 Skill Gap Analysis")

    skill_gap = []

    if sql_skill < 6:
        skill_gap.append("SQL")

    if dsa_skill < 6:
        skill_gap.append("DSA")

    if ml_skill < 6:
        skill_gap.append("Machine Learning")

    if len(skill_gap) == 0:
        st.success("No Major Skill Gaps Found")
    else:
        for skill in skill_gap:
            st.warning(skill)

    st.divider()

    st.subheader("📚 Recommended Learning Resources")

    if sql_skill < 6:
        st.write("SQLBolt")
        st.write("Mode Analytics SQL Tutorial")

    if dsa_skill < 6:
        st.write("LeetCode")
        st.write("NeetCode")

    if ml_skill < 6:
        st.write("Andrew Ng ML Course")
        st.write("Kaggle Learn")

    st.divider()

    st.subheader("🛣 Career Roadmap")

    roadmap = []

    if sql_skill < 6:
        roadmap.append("Master SQL")

    if dsa_skill < 6:
        roadmap.append("Solve 150+ DSA Problems")

    if ml_skill < 6:
        roadmap.append("Build ML Projects")

    roadmap.append("Complete Internship")
    roadmap.append("Build Portfolio")
    roadmap.append("Apply for Target Companies")

    for i, step in enumerate(roadmap, start=1):
        st.write(f"Month {i}: {step}")

    report = pd.DataFrame({
        "Metric": [
            "Career Match",
            "Readiness Score",
            "Resume Score",
            "Expected Salary"
        ],
        "Value": [
            best_role,
            readiness,
            resume_score,
            salary
        ]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        label="📥 Download Report",
        data=csv,
        file_name="career_report.csv",
        mime="text/csv"
    )

else:
    st.info("Fill details and click Generate Report")
