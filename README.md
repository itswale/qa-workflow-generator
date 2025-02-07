# QA Workflow Generator

## Description

The **QA Workflow Generator** is a Streamlit-based application that leverages ChatGPT, Make.com, and Airtable to automate the process of generating User Story workflows. The app processes data in real-time and automatically generates **Test Cases** and **Bug Reports**. It utilizes advanced integrations with AI and automation tools to streamline the workflow creation process for quality assurance teams.

## Features

- **User Story Workflow Generation**: Input a User Story and get a detailed workflow generated using ChatGPT.
- **Real-Time Data Processing**: Processes the data instantly and updates the workflow as you input new information.
- **Test Cases Generation**: Automatically creates test cases based on the User Story.
- **Bug Report Generation**: Generates bug reports from the test cases for easy tracking.
- **Seamless Integrations**: Built using **Make.com** for automation, **Airtable** for data management, and **ChatGPT API** for intelligent conversation handling.

## App Link

You can view and use the app at:

[QA Workflow Generator App](https://flowbot.streamlit.app/)

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **ChatGPT API**: For natural language processing and generating workflows, test cases, and bug reports.
- **Make.com**: For automating workflows.
- **Airtable**: For managing and storing the generated data.
- **Python**: For backend logic and integrations.

## Installation

To run this app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/qa-workflow-generator.git

2. Navigate to the project directory:

    cd qa-workflow-generator

3. Install the required dependencies:

    pip install -r requirements.txt

4. Run the Streamlit app:

    streamlit run app.py
