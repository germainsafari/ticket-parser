AI Ticket Parser (GPT-4 Powered)

This project leverages OpenAI’s GPT-4 to extract structured information from IT support tickets stored in .txt files.
It processes ticket details, issue descriptions, actions requested, and SQL queries into a structured format for easy analysis and automation.

🚀 Features

✅ Parses unstructured text from IT support tickets.
✅ Uses GPT-4 API for natural language understanding.
✅ Extracts ticket ID, customer, system details, requested actions, and SQL queries.
✅ Outputs structured results in a readable format.
✅ Designed for scalability (supports batch processing).

🛠️ Setup Instructions

Follow these steps to set up and run the project on MacOS or Windows.

1️⃣ Clone the Repository

git clone https://github.com/yourusername/ai_ticket_parser.git
cd ai_ticket_parser

2️⃣ Create a Virtual Environment

Mac/Linux

python3 -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies

Ensure you have Python 3.8+ installed. Then, run:

pip install -r requirements.txt

4️⃣ Set Up OpenAI API Key

GPT-4 requires an API key. Securely store it using a .env file.
1.	Create a .env file in the project root directory.
2.	Add your OpenAI API key inside the file:

OPENAI_API_KEY=your-api-key-here

```
3.	Modify main.py to read the API key securely:

```

from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

5️⃣ Add Ticket Files
1.	Create a tickets/ folder inside the project.
2.	Add .txt files containing support ticket content.

Example Ticket (tickets/ticket1.txt)

# Ticket PA123

P4
Customer: [a.customer@example.com](mailto:a.customer@example.com)

Issue:

- I created a project (P-6666)
- It is in the EPX acceptance by mistake.

Action requested:

- Please delete this.

# ===
Sql

Select * from project where project_id = 'P-6666' - 1 row returned
Delete * from project where project_id = 'P-6666' - 1 row affected

6️⃣ Run the Ticket Parser

Execute the script to process all .txt files:

python [main.py](http://main.py/)

The script will:
✔ Read all .txt files from the tickets/ directory.
✔ Process each file using GPT-4.
✔ Display structured output in the terminal.

📌 Example Output

# Title: Please delete the project :projectId

## Attributes

- TicketId: PA123
- Customer: [a.customer@example.com](mailto:a.customer@example.com)
- ProjectId: P-6666
- System: EPX
- Environment: acceptance

## SQL

- Check SQL: Select * from project where project_id = :projectId
- Resolve SQL: Delete * from project where project_id = :projectId

⚡ Error Handling & Logs
•	Handles missing or corrupted ticket files.
•	Logs API errors (e.g., rate limits, invalid keys).
•	Provides fallback processing if GPT-4 fails.

🚀 Future Enhancements

🔹 Save structured output to JSON or a database.
🔹 Deploy as a Flask API to process tickets via HTTP requests.
🔹 Improve prompt engineering for better extractions.
🔹 Implement multi-language support for diverse ticket sources.

📜 License

MIT License
