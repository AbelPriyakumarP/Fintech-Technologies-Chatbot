# 🚀 FinSolve AI Chatbot

FinSolve AI is a **secure, role-based, internal AI assistant designed specifically for FinTech enterprises**. Built on a **Retrieval-Augmented Generation (RAG)** architecture, it delivers fast, contextually relevant answers to HR, Finance, Marketing, and Technology queries — fully respecting role-based access control for internal data privacy.

![FinSolve AI Logo](https://th.bing.com/th/id/OIP.nukhjwUaGwnNDsCnykrM9wHaHa?w=209&h=209&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3)

---

## 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture Overview](#architecture-overview)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Usecases](#Usecases)
- [How it Works](#How-it-works)
- [Contributing](#contributing)
- [Let's Connect](#Let's-Connect)

---

## ✨ Features

✅ **Role-Based Access Control (RBAC)** — Displays answers and options tailored to each user's department and permission level.  
✅ **Secure Employee Authentication** — Simple name/password login, with future-ready scope for OAuth/SSO integrations.  
✅ **Modern, Accessible UI** — Responsive, gradient-themed interface with dark inputs and high-contrast text for readability.  
✅ **Real-Time Analytics** — Live dashboard with chat volumes, user activity, and engagement metrics.  
✅ **Chat History & Notes** — Save, download, or clear session chats and personal notes on the fly.  
✅ **Dynamic AI Suggestions** — Context-aware query recommendations based on user role and conversation flow.  
✅ **Downloadable Reports** — Export chat histories and notes in CSV or TXT formats for audit or review.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (custom styled)
- **Backend:** Python FastAPI (or Flask alternative)
- **AI Layer:** Retrieval-Augmented Generation (RAG) powered by LangChain + Groq(llama) API
- **Authentication:** Custom (with scope for OAuth2/JWT integration)
- **Visualization:** Streamlit + Plotly/Altair
- **Deployment:** Streamlit Cloud / Docker / Localhost

---

## 📖 Architecture Overview
![Image alt](https://github.com/AbelPriyakumarP/Fintech-Technologies-Chatbot/blob/4b9604153ed648b7560d9fd1c7e3a8e6a6f6c752/Architecture%20Overview.png)

## 📸 Screenshots

![Image alt](https://github.com/AbelPriyakumarP/FinTech-Company-ChatBot/blob/780049da202d0be0939ad283ec0ce6ca48f4e43a/resources/new%20ss.png)

---

## RAG Architecture

![Image alt](https://github.com/AbelPriyakumarP/FinTech-Company-ChatBot/blob/743d6b01be4000b3e092a46a444600f11ba6cb68/resources/rag%20flowchart.png)

## 🚀 Getting Started

### 📦 Prerequisites

- Python `3.8+`
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [requests](https://docs.python-requests.org/)
- Backend API running at `http://localhost:8000`

---

### 📥 Installation

```bash
git clone https://github.com/your-org/FinSolve-Company-ChatBot.git
cd FinSolve-Company-ChatBot
pip install -r requirements.txt
```
---

### 🗂️ Project Structure

![Image alt](https://github.com/AbelPriyakumarP/FinTech-Company-ChatBot/blob/595fe5c8744d137a2dcb744400a428fbddbb471c/workflow_diagram.png)

---

### Detailed Overview 

## 🔒 1️⃣ User Authentication
User enters Name & Password in Streamlit frontend.

Frontend sends credentials to User Access Control DB via RAG Backend API.

API validates credentials and retrieves role-based permissions.

On success → User redirected to main chat interface.

## 💬 2️⃣ Chat Query Submission
User types a query in the Streamlit Chat UI.

Query sent to RAG Backend API via REST call.

## 🔍 3️⃣ Contextual Retrieval (RAG Flow)
API uses role information from Access DB.

API sends query and role context to Vector Database (FAISS/Chroma).

Vector DB performs similarity search on relevant documents.

Top relevant results are retrieved as contextual passages.

## 🤖 4️⃣ AI Response Generation
Retrieved passages and user query passed to LLM (OpenAI/GPT-4 or equivalent) via LangChain RAG pipeline.

LLM generates a contextual, role-filtered answer.

API returns response to the Streamlit UI.

## 📊 5️⃣ Usage Analytics Logging
API logs each query, response, user info, timestamp to Analytics DB (could be SQLite/PostgreSQL/JSON initially).

Real-time stats reflected on Streamlit Analytics Dashboard (chat counts, queries per department, usage trends).

## 📄 6️⃣ Personal Notes & Chat History
Users can save private notes in session.

Notes and chat history stored temporarily or persistently.

Options to download notes and chats as CSV/TXT via frontend.

## 📈 7️⃣ Admin or Department Head Features
Special roles have additional dashboards:

See team-level analytics.

Download department chat histories.

Configure document uploads for Vector DB (future scope).

---

### 📖 API Documentation

Access the interactive API docs via FastAPI:

bash
Copy
Edit
http://localhost:8000/docs

---

### 📌 Use Cases
Here’s where and how FinSolve AI can be valuable in a FinTech enterprise setting:

✅ Employee Self-Service Helpdesk:
Employees instantly resolve HR, Finance, or IT-related queries without waiting for human support.

✅ HR Process Automation:
Provide onboarding, leave policies, benefits, payroll, and grievance resolution support through role-based access.

✅ Finance Department Q&A:
Handle employee questions about reimbursements, tax declarations, financial compliance, or budget processes.

✅ Marketing Team Assistance:
Answer FAQs on campaign performance, brand guidelines, and lead generation processes.

✅ Technical Support Automation:
Help engineers and IT staff resolve technical queries about deployment pipelines, code repositories, or data policies.

✅ Compliance & Risk FAQs:
Provide controlled, up-to-date regulatory guidelines and policies based on user role.

✅ Internal Knowledge Management:
Serve as a role-aware AI assistant for accessing internal SOPs, manuals, and policy documents.

✅ Analytics Reporting for Managers:
Department heads can monitor query trends, peak hours, and department activity with real-time analytics.

---
### ⚙️ How It Works
A step-by-step breakdown of how FinSolve AI functions internally:

1️⃣ User Login:
Employees log in using their name and password. The system verifies credentials via the User Access Control DB and retrieves their assigned role (e.g., HR, Finance, Tech, Marketing).

2️⃣ Role-Based Dashboard:
Post-login, users access a personalized chat interface with role-specific query suggestions and restricted access to internal documents.

3️⃣ Query Submission:
The user submits a question via the chat UI. The query is sent to the RAG-powered Backend API.

4️⃣ Context Retrieval (RAG):
The backend fetches the employee’s role and retrieves relevant internal documents or FAQs from a Vector Database (like FAISS/Chroma) using similarity search.

5️⃣ AI Response Generation:
The retrieved documents and the original query are sent to a large language model (e.g., GROQ via LangChain). The LLM generates a contextually accurate, role-filtered response.

6️⃣ Response Delivery:
The AI-generated response is returned to the Streamlit chat UI, displayed instantly to the employee.

7️⃣ Analytics Logging:
Each query, response, user, and timestamp are logged in the Analytics DB for reporting and activity insights.

8️⃣ Chat History & Notes:
Users can view, clear, download their chat history, and take private session notes for later reference.

9️⃣ Admin Features (For Managers):
Managers with special roles access dashboards for department-wise usage reports, chat volumes, and query trend analytics.



---
### 🤝 Contributing

We welcome contributions from the community!

Fork the repository

Create your feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m 'Add: New feature'

Push to the branch: git push origin feature/YourFeature

Open a Pull Request

---
### 🤝 Let’s Connect!

If you're passionate about **Generative AI, LangChain, LLMs, or Multimodal Agents**, feel free to connect:

* 📱 [LinkedIn][https://www.linkedin.com/in/yourprofile](https://www.linkedin.com/in/abel-priyakumar-p/)
