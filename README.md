

## **Setup Instructions & README.md**
```markdown
# AI Ticket Parser (GPT-4 Powered)

This project extracts structured information from IT support tickets stored in `.txt` files using OpenAI’s GPT-4 API.  
It processes ticket details, issue descriptions, actions requested, and SQL queries into structured output.

---

## **Setup Instructions**
Follow these steps to set up and run the project on **MacOS** or **Windows**.

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai_ticket_parser.git
cd ai_ticket_parser
```

---

### **2. Create a Virtual Environment**
#### **Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```
#### **Windows**
```powershell
python -m venv venv
venv\Scripts\activate
```

---

### **3. Install Required Libraries**
Run the following command inside your virtual environment:
```bash
pip install -r requirements.txt
```

---

### **4. Store OpenAI API Key Securely**
1. **Create a `.env` file** in the project root directory.
2. **Add the following line** to store your API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. **Modify `main.py` to read the API key** from `.env`:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
   ```

---

### **5. Add Ticket Files**
1. **Create a `tickets/` folder** inside the project.
2. **Add `.txt` files** with ticket content.

Example (`tickets/ticket1.txt`):
```
Ticket PA123
============
P4
Customer: a.customer@example.com

Issue:
* I created a project (P-6666)
* It is in the EPX acceptance by mistake.

Action requested:
* Please delete this.

===
Sql
===
Select * from project where project_id = 'P-6666' - 1 row returned
Delete * from project where project_id = 'P-6666' - 1 row affected
```

---

### **6. Run the Ticket Parser**
```bash
python main.py
```
The script will:
1. Read all `.txt` files from the `tickets/` directory.
2. Process each file using GPT-4.
3. Display structured output in the terminal.

---

### **7. Example Output**
```
# Title: Please delete the project :projectId

## Attributes
- TicketId: PA123
- Customer: a.customer@example.com
- ProjectId: P-6666
- System: EPX
- Environment: acceptance

## SQL
- Check SQL: Select * from project where project_id = :projectId
- Resolve SQL: Delete * from project where project_id = :projectId
```

---

## **Future Enhancements**
- Save structured output to **JSON or database**.
- Deploy as a **Flask API** to process tickets in real-time.
- Improve **prompt engineering** for better extractions.

---

## **License**
MIT License
```

---

## **Final Thoughts**
- The script now **reads ticket files from a folder**, making it scalable.
- The **virtual environment ensures dependency isolation**.
- The **API key is stored securely** in a `.env` file.
- You can **easily test new tickets** by adding `.txt` files.

Would you like me to **extend this into a Flask API** so you can process tickets dynamically? 🚀