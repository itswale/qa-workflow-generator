import streamlit as st
import requests
import pandas as pd
from io import BytesIO
from fpdf import FPDF
import time  # For simulating delays
import random  # For dynamic generation

# Title and disclaimer
st.title("Automated QA Workflow Generator")
st.warning("⚠️ Data will not persist after you refresh the page. Please download your generated data.")

# Initialize session state for API usage, data storage, and generated story
if "api_usage" not in st.session_state:
    st.session_state["api_usage"] = 0  # Track the number of API calls made
if "data" not in st.session_state:
    st.session_state["data"] = []
if "generated_story" not in st.session_state:
    st.session_state["generated_story"] = ""

# Function to simulate sending the user story to Make.com and returning generated data
def generate_data(user_story, status):
    webhook_url = "https://hook.eu2.make.com/mqn5fcre0kw1occutd9mhnw65hieuktf"
    payload = {"user_story": user_story, "status": status}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        # Here we simulate the fetched results with a label "Fetched" to distinguish them
        return {
            "User Story": user_story,
            "Status": status,
            "Test Case": f"Fetched Test Case for {user_story}",
            "Bug Report": f"Fetched Bug Report for {user_story}"
        }
    else:
        st.error(f"Failed to submit. Error: {response.status_code}, Response: {response.text}")
        return None

# Function to generate a user story dynamically using your variables
def generate_user_story():
    role = ["user", "admin", "guest", "editor", "moderator"]
    action = ["reset my password", "view my dashboard", "receive notifications", "edit my profile", "export data"]
    goal = ["maintain security", "track my progress", "stay updated", "personalize my experience", "analyze the results"]
    return f"As a {random.choice(role)}, I want to {random.choice(action)}, so that I can {random.choice(goal)}."

# Button to generate a user story (updates session state)
if st.button("Generate User Story"):
    st.session_state["generated_story"] = generate_user_story()

# The submission form uses one text area for either manual input or the generated story.
with st.form("user_story_form"):
    user_story = st.text_area("User Story",
                              value=st.session_state.get("generated_story", ""),
                              placeholder="As a user, I want to...",
                              height=150)
    # User can select the status regardless of how the story was created.
    status = st.selectbox("Select Status", ["Pending", "Processed"], index=0)
    submit_button = st.form_submit_button("Submit User Story")

# When the submit button is clicked, we simulate two phases:
#   1. Submission of the user story.
#   2. Fetching the test case and bug report data.
if submit_button:
    if user_story and status:
        # Phase 1: Simulate submission delay (e.g., 5 seconds)
        with st.spinner("Submitting user story... Please wait for 5 seconds."):
            time.sleep(5)
        st.info("User story submitted. Now fetching test cases and bug reports...")
        
        # Phase 2: Simulate fetching delay (e.g., 10 seconds) with a progress bar.
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.1)  # Total ~10 seconds delay
            progress_bar.progress(i + 1)
        
        # Once the simulated fetching is complete, call generate_data() to get the dummy results.
        generated_data = generate_data(user_story, status)
        if generated_data:
            st.session_state["api_usage"] += 1
            st.session_state["data"].append(generated_data)
            st.success("User story submitted successfully and data generated!")
    else:
        st.warning("Please enter a user story and select a status.")

# Display generated data and provide download options.
if st.session_state["data"]:
    st.subheader("Generated Data")
    df = pd.DataFrame(st.session_state["data"])
    st.dataframe(df)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data as CSV", data=csv, file_name="generated_data.csv", mime="text/csv")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Generated Data", ln=True, align='C')
    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"User Story: {row['User Story']}", ln=True)
        pdf.cell(200, 10, txt=f"Status: {row['Status']}", ln=True)
        pdf.cell(200, 10, txt=f"Test Case: {row['Test Case']}", ln=True)
        pdf.cell(200, 10, txt=f"Bug Report: {row['Bug Report']}", ln=True)
        pdf.cell(200, 10, txt=" ", ln=True)
    
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S').encode('latin1'))
    pdf_output.seek(0)
    st.download_button("📄 Download Data as PDF", data=pdf_output, file_name="generated_data.pdf", mime="application/pdf")

# Display API usage status.
st.subheader("API Usage Status")
usage = st.session_state["api_usage"]
max_usage = 100
st.progress(usage / max_usage)
st.text(f"{usage}/{max_usage} requests used.")
