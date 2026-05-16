import streamlit as st
import pandas as pd

# PAGE SETTINGS

st.set_page_config(
    page_title="MediSphere AI",
    layout="wide"
)

# TITLE

st.title("🏥 MediSphere AI")
st.subheader("Future Healthcare Intelligence Platform")

# SIDEBAR MENU

menu = st.sidebar.selectbox(

    "Navigation",

    [
        "Home",
        "AI Chatbot",
        "Risk Analysis",
        "Emergency Support"
    ]
)

# HOME PAGE

if menu == "Home":

    st.header("Welcome to MediSphere AI")

    st.write("""
MediSphere AI is an intelligent healthcare platform powered by:
- Machine Learning
- Agentic AI
- RAG Architecture
- Healthcare Analytics
""")

    st.info("""

👋 How to Use

1. Open the sidebar menu
2. Select a module
3. Enter healthcare questions or symptoms
4. View AI-generated insights

""")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Patients Processed",
        "12,540"
    )

    col2.metric(
        "Critical Cases",
        "1,240"
    )

    col3.metric(
        "AI Accuracy",
        "87%"
    )

    chart_data = pd.DataFrame({

        "Department": [
            "Cardiology",
            "Diabetes",
            "Respiratory",
            "Emergency"
        ],

        "Cases": [
            300,
            250,
            170,
            140
        ]
    })

    st.bar_chart(
        chart_data.set_index("Department")
    )

# AI CHATBOT

elif menu == "AI Chatbot":

    st.header("Healthcare AI Assistant")

    question = st.text_input(

        "Ask healthcare question",

        placeholder="Example: What are symptoms of diabetes?"
    )

    if st.button("Generate Response"):

        if "diabetes" in question.lower():

            st.success("""
Possible diabetes symptoms:
- fatigue
- frequent urination
- increased thirst
- blurred vision

Please consult a doctor for diagnosis.
""")

        elif "chest pain" in question.lower():

            st.error("""
🚨 Emergency symptoms detected.

Please seek immediate medical attention.
""")

        elif "fever" in question.lower():

            st.info("""
Fever may occur due to infections or inflammation.
Stay hydrated and monitor body temperature.
""")

        else:

            st.warning("""
Please consult healthcare professionals for accurate diagnosis.
""")

# RISK ANALYSIS

elif menu == "Risk Analysis":

    st.header("Patient Risk Analysis")

    age = st.slider(
        "Patient Age",
        1,
        100,
        50
    )

    admissions = st.slider(
        "Previous Admissions",
        0,
        10,
        1
    )

    if st.button("Analyze Risk"):

        risk_score = 0

        if age > 60:
            risk_score += 40

        if admissions > 2:
            risk_score += 50

        if risk_score >= 70:

            st.error("🔴 High Readmission Risk")

        elif risk_score >= 40:

            st.warning("🟠 Moderate Risk")

        else:

            st.success("🟢 Low Risk")

        st.progress(risk_score / 100)

        st.write(
            f"AI Risk Score: {risk_score}%"
        )

# EMERGENCY SUPPORT

elif menu == "Emergency Support":

    st.header("Emergency Guidance")

    symptoms = st.text_area(

        "Enter symptoms",

        placeholder="Example: chest pain, breathing difficulty"
    )

    if st.button("Check Emergency"):

        emergency_words = [
            "chest pain",
            "breathing",
            "stroke",
            "heart attack"
        ]

        found = False

        for word in emergency_words:

            if word in symptoms.lower():

                found = True

        if found:

            st.error("""
🚨 Emergency symptoms detected.

Contact emergency services immediately.
""")

        else:

            st.success("""
No major emergency indicators detected.
""")

# FOOTER

st.markdown("---")

st.caption("""
MediSphere AI

Built using:
- Streamlit
- Machine Learning
- Agentic AI
- RAG Concepts
""")
