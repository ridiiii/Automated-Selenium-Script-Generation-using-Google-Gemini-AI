# Automated-Selenium-Script-Generation-using-Google-Gemini-AI
Overview

This project automates the generation of Python Selenium scripts by leveraging Google's Gemini AI (Generative AI). Given a set of test cases stored in an Excel file, the script interacts with Gemini to generate fully functional Selenium test scripts.



Approach

Reading Test Cases:

-The script loads test cases from an Excel file (test_cases.xlsx) using Pandas.

-Each test case consists of a Test Scenario and Steps to Execute.

Generating Selenium Scripts:

-The script constructs a structured prompt including test details and formatting instructions.

-It then calls Gemini’s API (gemini-1.5-pro-latest) to generate a Selenium script for each test case.

-AI-generated scripts include WebDriver initialization, element interactions, assertions, and stability mechanisms (e.g., WebDriverWait).

Saving the Generated Scripts:

-The generated scripts are stored in an Excel file (test_scripts.xlsx) with two columns: Test Case ID and Python Selenium Code.

-If the API fails for a specific test case, an error message is logged in the output file.




Challenges Faced

-Access to Gemini API:

-Direct API access may be restricted.

-As a workaround, I manually tested prompts using Google's web-based GenAI tool.

Ensuring Structured Output:

-AI-generated code can be inconsistent.

-To address this, I refined the prompt to enforce strict formatting and require working Selenium code.

Handling API Failures:

-The script includes exception handling to prevent crashes.

-If an API request fails, the script logs the error and continues processing the remaining test cases.





How to Run the Script

Prerequisites

-Python 3.8+

-Required Python libraries: pandas, google-generativeai, openpyxl

-Selenium WebDriver (e.g., ChromeDriver, GeckoDriver)

-Gemini API Key (set as an environment variable: GEMINI_API_KEY)
