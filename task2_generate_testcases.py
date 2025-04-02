import google.generativeai as genai
import os
import json
import re
import pandas as pd  # pandas for Excel generation

# Load API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is not set. Please set it as an environment variable.")

genai.configure(api_key=API_KEY)

# model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Debugging: Print API key status
print(" Using API Key:", API_KEY[:6] + "****")

# Define the prompt
prompt = """
Generate 3 meaningful test cases for a login page in valid JSON format without markdown formatting.
Each test case should have:
- Test Case ID
- Test Scenario
- Steps to Execute
- Expected Result
"""

try:
    # 🔹 Call the Gemini API
    response = model.generate_content(prompt)
    
    # 🔹 Check if response is valid
    if not response or not response.candidates:
        raise ValueError("Empty response received from Gemini API.")
    
    # 🔹 Extract the text response
    test_cases_text = response.candidates[0].content.parts[0].text.strip()

    # 🔹 Remove Markdown formatting (e.g., ```json and ```)
    test_cases_text = re.sub(r"```json|```", "", test_cases_text).strip()

    print("Cleaned API Response:\n", test_cases_text)  # Debugging: Show cleaned response

    # 🔹 Convert to JSON
    test_cases = json.loads(test_cases_text)

    # 🔹 Convert JSON to DataFrame
    df = pd.DataFrame(test_cases)

    # 🔹 Save to Excel
    excel_filename = "test_cases.xlsx"
    df.to_excel(excel_filename, index=False)

    print(f"Test cases successfully saved in {excel_filename}!")

except json.JSONDecodeError:
    print("Error: Response is not in valid JSON format.")
except Exception as e:
    print(f"Error generating test cases: {e}")
