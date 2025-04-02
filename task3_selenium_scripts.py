import google.generativeai as genai
import pandas as pd
import json
import os

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(" GEMINI_API_KEY is not set. Please set it in your environment variables.")

genai.configure(api_key=API_KEY)

def generate_selenium_scripts(test_cases_file):
    
    
    df = pd.read_excel(test_cases_file)

    selenium_scripts = []

    for index, row in df.iterrows():
        test_scenario = row['Test Scenario']
        steps = str(row['Steps to Execute'])  # Ensure steps are treated as a string

        # Enhanced Prompt
        prompt = f"""
        Generate a **complete** Python Selenium test script based on the following test case:
        - **Test Scenario:** {test_scenario}
        - **Steps to Execute:**
        {steps}

        🔹 **Requirements:**
        - Use `selenium` library.
        - Ensure `WebDriverWait` for stable element interactions.
        - Add assertions based on expected outcomes.
        - **Do NOT include placeholders**; generate a working script.

        **Output Format:**
        ```python
        # Python Selenium Script
        <GENERATED CODE>
        ```
        """

        try:
            # Call Gemini API
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(prompt)

            # Extract response
            selenium_script = response.text.strip()

            # Append script
            selenium_scripts.append({
                "Test Case ID": row['Test Case ID'],
                "Python Selenium Code": selenium_script
            })

        except Exception as e:
            print(f"Error generating script for {row['Test Case ID']}: {e}")
            selenium_scripts.append({
                "Test Case ID": row['Test Case ID'],
                "Python Selenium Code": f"Error: {e}"
            })

    # Save scripts to Excel
    script_df = pd.DataFrame(selenium_scripts)
    script_df.to_excel("test_scripts.xlsx", index=False)
    print(" Selenium scripts generated and saved to test_scripts.xlsx!")


generate_selenium_scripts("test_cases.xlsx")
