import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (Required for openai>=1.0.0)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def extract_ticket_info(ticket_text):
    """Uses OpenAI GPT to extract structured information from a Jira ticket."""
    prompt = f"""
    Extract structured information from the following IT support ticket:

    ``` 
    {ticket_text}
    ```

    **Format the output in Markdown like this:**
    ```
    # Title: <Generated Title>

    ## Attributes
    - TicketId: <ticket_id>
    - Customer: <customer_email>
    - ProjectId: <project_id>
    - ItemId: <item_id>
    - System: <system>
    - Environment: <environment>
    - OldValue: <old_value>
    - NewValue: <new_value>

    ## SQL
    - Check SQL: <SQL_check>
    - Resolve SQL: <SQL_resolve>
    ```
    - Ensure "System" and "Environment" are correctly extracted separately.
    - Ensure that "P4" is not mistakenly assigned as a ProjectId.
    - Replace missing fields with `"N/A"` if unavailable.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured information from IT support tickets."},
                {"role": "user", "content": prompt}
            ]
        )

        # Ensure response is valid
        if not response or not response.choices or not response.choices[0].message.content.strip():
            return "⚠️ Error: Empty response from OpenAI API. Please check API limits or response handling."

        return response.choices[0].message.content

    except openai.OpenAIError as e:
        return f"⚠️ OpenAI API Error: {str(e)}"

def process_ticket_files(directory="tickets"):
    """Reads all ticket text files in a directory and processes them."""
    if not os.path.exists(directory):
        print(f"⚠️ Directory '{directory}' not found. Please create it and add ticket files.")
        return

    ticket_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

    if not ticket_files:
        print("⚠️ No ticket files found in 'tickets/' folder. Please add some .txt files.")
        return

    for idx, ticket_file in enumerate(ticket_files, start=1):
        with open(os.path.join(directory, ticket_file), "r", encoding="utf-8") as file:
            ticket_text = file.read().strip()  # Remove unnecessary whitespace
        
        print(f"\n--- Processing Ticket {idx}: {ticket_file} ---")
        output = extract_ticket_info(ticket_text)
        print(output)
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    process_ticket_files()
