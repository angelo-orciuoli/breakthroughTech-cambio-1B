# Entrepreneur Compass Tool

The "Entrepreneur Compass Tool" is a web application built with Streamlit that serves as a personalized resource navigator for aspiring entrepreneurs.

- **Core Functionality:** It presents users with a detailed survey about their background, business ideas, and needs.
- **Outcome:** Based on their survey responses, the application identifies and displays a tailored list of entrepreneurship programs, resources, and funding opportunities that they are eligible for.
- **Technology Stack:** The application is written in Python and uses the following key libraries:
  - `streamlit`: For building the interactive web interface.
  - `pandas`: For data manipulation.
  - `gspread` and `google-auth`: For interacting with the Google Sheets API to store survey responses.

---

## Getting Started & Local Setup

To run the project locally, follow these steps:

**Prerequisites:**
- Python 3.x installed.
- A Google Cloud Platform (GCP) project with the Google Sheets API and Google Drive API enabled.
- A Google service account with credentials.

**Setup Instructions:**

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd breakthroughTech-cambio-1B
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Google Cloud Credentials:**
    - The file `cambio_creds_template.json` is a template for the Google Cloud service account credentials.
    - Create a copy of it named `cambio_creds.json` and populate it with the actual credentials from your GCP service account.
    - **Important:** The `cambio_creds.json` file is already listed in `.gitignore` to prevent committing sensitive credentials. Do not remove it from the gitignore.
4.  **Set up the Google Sheet:**
    - Create a new Google Sheet to store the survey responses.
    - Share this sheet with the `client_email` found in your `cambio_creds.json` file, giving it "Editor" permissions.
    - Open `rough_prototype.py` and replace the placeholder in `sheet_id = "   "` with your Google Sheet's ID.
5.  **Run the application:**
    ```bash
    streamlit run rough_prototype.py
    ```
    The application will now be running and accessible in your web browser.

---

## Codebase Overview

The entire application logic is currently contained within `rough_prototype.py`.

- **Initialization and Authentication:** Imports libraries, authenticates with the Google Sheets API, and opens the target spreadsheet.
- **Streamlit App Configuration:** Sets up the Streamlit page and initializes all variables that will store the user's survey responses.
- **Survey Questions (UI):** Defines the survey using various Streamlit input widgets.
- **Submission Logic:** When the "Submit" button is clicked, the user's data is collected, appended to the Google Sheet, and a series of `if` statements determine which resources to display.

---

## Actionable Next Steps & Deliverables

The current version is a functional prototype. The following steps are designed to mature the codebase into a robust and maintainable application.

### Milestone 1: Code Refactoring and Configuration Management

The goal of this milestone is to move from a single-script prototype to a modular, configurable, and easily maintainable application structure.

-   **Deliverable 1.1: Modular Code Structure**
    -   **Task:** Decompose `rough_prototype.py` into multiple, single-responsibility files.
        -   `app.py`: The main entry point for the Streamlit application. It will import and call functions from the other modules.
        -   `ui.py`: Will contain all functions that render Streamlit UI components (e.g., `render_survey_page()`).
        -   `google_sheets_client.py`: Will handle all interactions with the Google Sheets API (authentication, writing data).
        -   `eligibility_rules.py`: Will contain the logic for matching users to programs based on their survey responses.
        -   `config.py`: Will store all configuration variables and constants (Google Sheet ID, credentials path, etc.).

-   **Deliverable 1.2: Dynamic Eligibility Logic**
    -   **Task:** Decouple the hardcoded eligibility rules from the application logic.
        -   Read the program requirements from the `data/program_requirements.xlsx` file into a pandas DataFrame at startup.
        -   In `eligibility_rules.py`, create a function that takes the user's survey data as input, compares it against the rules in the DataFrame, and returns a list of eligible programs. This will replace the long `if/elif/else` chain.

-   **Deliverable 1.3: Input Validation and Error Handling**
    -   **Task:** Implement server-side validation for user inputs.
        -   Add validation for required fields to ensure they are not submitted empty.
        -   Use regular expressions to validate the format of email addresses and phone numbers.
        -   Implement try-except blocks in `google_sheets_client.py` to gracefully handle potential API errors (e.g., authentication failure, sheet not found).

### Milestone 2: Enhancing User Experience (UX)

This milestone focuses on improving the user's journey through the application, from filling out the survey to viewing the results.

-   **Deliverable 2.1: Improved Feedback on Submission**
    -   **Task:** Provide clear feedback to the user during and after form submission.
        -   Use `st.spinner()` to show a loading indicator while the data is being sent to Google Sheets.
        -   Display a clear `st.success()` or `st.balloons()` message upon successful submission.
        -   If an error occurs, display a user-friendly `st.error()` message.

-   **Deliverable 2.2: Redesigned Results Page**
    -   **Task:** Transform the results from a simple list of links into a more informative and visually appealing layout.
        -   Use `st.columns`, `st.container`, and `st.expander` to create "cards" for each recommended program.
        -   Each card should include the program name, a brief description (pulled from the `program_requirements.xlsx` file), and a clickable link.

### Milestone 3: Testing, Documentation, and Deployment Prep

The final milestone ensures the application is reliable, well-documented, and ready for deployment.

-   **Deliverable 3.1: Unit Testing**
    -   **Task:** Create a test suite for the core application logic.
        -   Write unit tests for the functions in `eligibility_rules.py`. Use sample user data to assert that the correct programs are recommended for various scenarios. This will ensure that changes to the rules don't break existing logic.

-   **Deliverable 3.2: Code Documentation**
    -   **Task:** Add comprehensive documentation to the new, modular codebase.
        -   Write clear docstrings for all functions and modules, explaining their purpose, arguments, and return values.
        -   Add inline comments where the code is complex or non-obvious.

-   **Deliverable 3.3: Deployment Guide**
    -   **Task:** Create a step-by-step guide for deploying the application.
        -   Write deployment instructions for a platform like Streamlit Cloud, including how to manage dependencies and secrets (like the Google service account credentials).
        -   Alternatively, create a `Dockerfile` to containerize the application for deployment on other cloud platforms.