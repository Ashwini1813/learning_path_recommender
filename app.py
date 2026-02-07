import streamlit as st
from recommender import LearningPathRecommender

recommender = LearningPathRecommender("data/courses.csv")

st.title("Learning Path Recommender")

goal = st.selectbox(
    "Select your career goal:",
    ["Data Science", "Web Development", "AI Engineer"]
)

level = st.selectbox(
    "Select your current level:",
    ["Beginner", "Intermediate", "Advanced"]
)

skills_input = st.text_input(
    "Enter your current skills (comma separated):",
    "Python, Statistics"
)

if st.button("Recommend Learning Path"):
    skills = [s.strip() for s in skills_input.split(",")]

    st.subheader("Recommended Learning Path")
    path = recommender.recommend_path(goal, level)

    for i, row in path.iterrows():
        st.write(f"- {row['course_name']} ({row['level']})")

    st.subheader("Skill Gaps")
    gaps = recommender.skill_gap(skills, goal)

    if gaps:
        for g in gaps:
            st.write(f"- {g}")
    else:
        st.write("You already have all required skills!")
