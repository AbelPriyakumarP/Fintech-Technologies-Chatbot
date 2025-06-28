import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- Streamlit App for FinSolve AI Chatbot ---
st.set_page_config(
    page_title="FinSolve Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- Custom CSS for Purple Gradient Image Background Theme ---
st.markdown("""
    <style>
    body, .stApp {
        background: url('https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1024&q=80') no-repeat center center fixed !important;
        background-size: cover !important;
        color: #e0e6ed !important;
    }
    .block-container, .main, .st-cq, .st-bf, .st-b8, .st-b7, .st-b6, .st-b5, .st-b4, .st-b3, .st-b2, .st-b1, .st-b0 {
        background: rgba(30, 0, 50, 0.82) !important;
    }
    .st-emotion-cache-1kyxreq, .st-emotion-cache-13ln4jf, .st-emotion-cache-1v0mbdj, .st-emotion-cache-1wrcr25 {
        background: rgba(30, 0, 50, 0.82) !important;
    }
    .neon-header {
        font-family: 'Orbitron', sans-serif;
        color: #e0e6ed !important;
        text-shadow: none !important;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
        letter-spacing: 1px;
    }
    .neon-sub {
        color: #cfc6e6 !important;
        text-shadow: none !important;
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .chat-bubble-user {
        background: rgba(80, 30, 120, 0.85);
        border-radius: 15px 15px 0 15px;
        box-shadow: 0 0 10px #6c3bb8;
        text-align: left;
        border: 1px solid #b18fff;
        color: #fff !important;
        margin-bottom: 0.7rem !important;
        margin-top: 0.7rem !important;
        padding: 0.7rem 1rem !important;
    }
    .chat-bubble-bot {
        background: rgba(60, 0, 90, 0.85);
        border-radius: 15px 15px 15px 0;
        box-shadow: 0 0 10px #6c3bb8;
        text-align: left;
        border: 1px solid #b18fff;
        color: #fff !important;
        margin-bottom: 1.2rem !important;
        padding: 0.7rem 1rem !important;
    }
    .history-sidebar, .stExpander, .stExpanderHeader, .stExpanderContent {
        background: rgba(40, 0, 60, 0.85) !important;
        border-radius: 15px !important;
        color: #e0e6ed !important;
    }
    .dashboard-widget, .user-info-box, .stMetric, .stTextArea, .stTextInput, .stSelectbox, .stButton, .stDownloadButton {
        background: rgba(40, 0, 60, 0.85) !important;
        border-radius: 10px !important;
        color: #e0e6ed !important;
        border: 2px solid #b18fff !important;
        box-shadow: 0 0 10px #6c3bb8;
    }
    .stButton>button, .stDownloadButton>button {
        background: rgba(80, 30, 120, 0.85) !important;
        color: #fff !important;
        border-radius: 8px !important;
        border: 1px solid #b18fff !important;
        font-weight: bold !important;
        transition: background 0.2s !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        background: rgba(120, 60, 180, 0.95) !important;
        color: #fff !important;
        border: 1px solid #fff !important;
    }
    .stSelectbox > div > div > div > input,
    .stSelectbox .css-1n76uvr, .stSelectbox .css-1wa3eu0 {
        color: #fff !important;
        background: rgba(60, 0, 90, 0.85) !important;
        border-radius: 6px !important;
        border: 2px solid #b18fff !important;
        caret-color: #fff !important;
    }
    .stSelectbox svg {
        color: #b18fff !important;
    }
    .stTextInput>div>input[type="password"], .stTextInput>div>input[type="text"] {
        background: rgba(60, 0, 90, 0.85) !important;
        color: #fff !important;
        border: 2px solid #b18fff !important;
        border-radius: 6px !important;
        caret-color: #fff !important;
    }
    .block-container > div > div:nth-child(2) * {
        color: #e0e6ed !important;
    }
    .chat-bubble-user, .chat-bubble-bot {
        color: #fff !important;
    }
    /* REMOVE custom chat input box style to use Streamlit default */
    /* [data-testid="stChatInput"] textarea,
    textarea[aria-label="Type your question and press Enter..."] {
        background: #111 !important;
        color: #fff !important;
        border: 2px solid #b18fff !important;
        border-radius: 8px !important;
        caret-color: #fff !important;
    } */
    .stTextArea>div>textarea {
        background: rgba(60, 0, 90, 0.85) !important;
        color: #fff !important;
        border: 2px solid #b18fff !important;
        border-radius: 6px !important;
        caret-color: #fff !important;
    }
    .user-info-box {
        background: rgba(40, 0, 60, 0.85) !important;
        border-radius: 10px !important;
        padding: 0.7rem 1rem 0.7rem 1rem !important;
        margin-bottom: 1rem !important;
        color: #fff !important;
        border: 2px solid #b18fff !important;
    }
    .stMetric {
        background: rgba(40, 0, 60, 0.85) !important;
        border-radius: 8px !important;
        padding: 0.5rem 0.7rem !important;
        margin-bottom: 0.5rem !important;
        color: #e0e6ed !important;
    }
    section[data-testid="stSidebar"] * {
        color: #fff !important;
    }
    .block-container > div > div:first-child * {
        color: #e0e6ed !important;
    }
    .stExpanderHeader, .stExpanderContent {
        background: rgba(40, 0, 60, 0.85) !important;
        color: #e0e6ed !important;
    }
    .stSidebar, .stSidebarContent, .stSidebarContainer {
        background: rgba(30, 0, 50, 0.82) !important;
    }
    /* Remove extra space on right of download buttons */
    .stDownloadButton, .stDownloadButton button {
        width: 100% !important;
        margin-right: 0 !important;
        margin-left: 0 !important;
        display: block !important;
    }
    </style>
""", unsafe_allow_html=True)
# --- Load HR Data for Dropdown ---
try:
    hr_df = pd.read_csv("resources/data/hr/hr_data.csv", header=None)
    names = hr_df[1].dropna().unique().tolist()
except Exception:
    hr_df = pd.DataFrame()
    names = []

# --- Session State ---
if "user_info" not in st.session_state:
    st.session_state.user_info = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "full_name" not in st.session_state:
    st.session_state.full_name = ""
if "notes" not in st.session_state:
    st.session_state.notes = ""
if "login_error" not in st.session_state:
    st.session_state.login_error = ""
if "show_password" not in st.session_state:
    st.session_state.show_password = False
if "usage_analytics" not in st.session_state:
    st.session_state.usage_analytics = {"total_chats": 0, "total_users": 0, "total_responses": 0}
if "login_time" not in st.session_state:
    st.session_state.login_time = None

# --- Usage Analytics Update ---
def update_usage_analytics():
    st.session_state.usage_analytics["total_chats"] = len(st.session_state.chat_history)
    st.session_state.usage_analytics["total_responses"] = len([c for c in st.session_state.chat_history if c.get("response")])
    st.session_state.usage_analytics["total_users"] = 1 if st.session_state.user_info else 0

update_usage_analytics()

# --- Role-based Access Control Function ---
def check_role_access(query, user_info):
    role = user_info.get("role", "").lower()
    dept = user_info.get("department", "").lower()
    access_map = {
        "finance": ["finance", "financial", "revenue", "cost", "budget", "invoice", "profit", "loss"],
        "marketing": ["marketing", "campaign", "customer acquisition", "brand", "promotion", "advertising"],
        "hr": ["hr", "human resource", "leave", "attendance", "employee", "payroll", "manager"],
        "sales": ["sales", "target", "conversion", "lead", "deal", "region", "quota"]
    }
    for area, keywords in access_map.items():
        if any(kw in query.lower() for kw in keywords):
            if area not in role and area not in dept:
                return False
    return True

# --- Sidebar: Dashboard & Analytics (Right Sidebar) ---
with st.sidebar:
    st.markdown('<div style="text-align:center;">'
                '<img src="https://th.bing.com/th/id/OIP.nukhjwUaGwnNDsCnykrM9wHaHa?w=209&h=209&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" width="80" style="border-radius:30%;box-shadow:0 0 20px #6c3bb8;margin-bottom:0.5rem;">'
                '</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div>
            <div class="neon-header" style="font-size:1.3rem;color:#e0e6ed !important;">FinSolve AI</div>
            <div class="neon-sub" style="font-size:1rem;color:#cfc6e6 !important;">Your Secure Internal Chatbot</div>
            <hr style="border-color:#b18fff;">
        </div>
        """, unsafe_allow_html=True
    )
    if st.session_state.user_info:
        st.markdown(
            f"""<div style="color:#fff">
            <b>Welcome, {st.session_state.user_info['full_name']}!</b><br>
            <b>Role:</b> {st.session_state.user_info['role']}<br>
            <b>Dept:</b> {st.session_state.user_info['department']}
            </div>""", unsafe_allow_html=True)
        if st.button("Logout", use_container_width=True, key="logout_btn"):
            st.session_state.user_info = None
            st.session_state.full_name = ""
            st.session_state.login_error = ""
            st.session_state.login_time = None
            st.rerun()
        st.markdown('<hr style="border-color:#b18fff;">', unsafe_allow_html=True)
        st.markdown('<div class="dashboard-widget" style="color:#e0e6ed;"><b>Usage Analytics</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#e0e6ed">', unsafe_allow_html=True)
        st.metric("Total Chats", st.session_state.usage_analytics["total_chats"])
        st.metric("Total Users", st.session_state.usage_analytics["total_users"])
        st.metric("Total Responses", st.session_state.usage_analytics["total_responses"])
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<hr style="border-color:#b18fff;">', unsafe_allow_html=True)
        st.markdown(
            """
            <span style="color:#cfc6e6"><b>💡 Tips:</b>
            <ul>
                <li>Ask about HR, Finance, Marketing, or Tech.</li>
                <li>Role-based access is enforced.</li>
                <li>All chats are confidential.</li>
            </ul>
            </span>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown('<div style="color:#e0e6ed">Please login to access features.</div>', unsafe_allow_html=True)

# --- Main Layout ---
with st.container():
    left_col, main_col = st.columns([1.2, 2.8], gap="large")
    with left_col:
        if st.session_state.user_info:
            with st.expander("📜 Chat History", expanded=True):
                if st.button("🗑️ Clear Chat History", key="clear_history_btn", use_container_width=True):
                    st.session_state.chat_history = []
                    st.success("Chat history cleared.")
                    update_usage_analytics()
                if st.session_state.chat_history:
                    for chat in st.session_state.chat_history:
                        st.markdown(f'<div class="chat-bubble-user">🧑‍💼 {chat["query"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="chat-bubble-bot">🤖 {chat["response"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="color:#e0e6ed;text-align:center;">No chat history yet.<br>Your previous questions and answers will appear here.</div>', unsafe_allow_html=True)
            st.markdown('<div class="dashboard-widget"><b>Usage Analytics</b></div>', unsafe_allow_html=True)
            st.metric("Total Chats", st.session_state.usage_analytics["total_chats"])
            st.metric("Total Responses", st.session_state.usage_analytics["total_responses"])

    with main_col:
        st.markdown(
            '<div style="text-align:center;">'
            '<img src="https://th.bing.com/th/id/OIP.nukhjwUaGwnNDsCnykrM9wHaHa?w=209&h=209&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" width="110" style="border-radius:30%;box-shadow:0 0 30px #6c3bb8;margin-bottom:0.5rem;">'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown('<div class="neon-header">FinSolve Chatbot</div>', unsafe_allow_html=True)
        st.markdown('<div class="neon-sub">Ask me anything about your company, based on your access rights.</div>', unsafe_allow_html=True)

        # --- Login Input and User Name Access ---
        if not st.session_state.user_info:
            st.markdown("### 🔐 Login")
            if names:
                full_name = st.selectbox("🔑 Select Your FullName", names, key="sidebar_full_name", format_func=lambda x: x, label_visibility="visible")
            else:
                full_name = st.text_input("🔑 Select Your FullName", key="sidebar_full_name", max_chars=50, label_visibility="visible")
            pw_col1, pw_col2 = st.columns([4,1])
            with pw_col1:
                password = st.text_input("🔒 Password", type="password" if not st.session_state.show_password else "default", value="", max_chars=20, key="sidebar_password", help="Try: 1234", label_visibility="visible")
            with pw_col2:
                st.session_state.show_password = st.checkbox("Show", value=st.session_state.show_password, label_visibility="collapsed")
            login_btn = st.button("Login", use_container_width=True)
            if login_btn:
                if not full_name or not password:
                    st.session_state.login_error = "Please select your name and enter password."
                elif password != "1234":
                    st.session_state.login_error = "Incorrect password. Try: 1234"
                else:
                    try:
                        if not hr_df.empty:
                            user_row = hr_df[hr_df[1].str.strip().str.lower() == full_name.strip().lower()]
                            if user_row.empty:
                                st.session_state.login_error = "Login failed: User not found. Please contact HR."
                            else:
                                user_info = {
                                    "employee_id": user_row.iloc[0, 0],
                                    "full_name": user_row.iloc[0, 1],
                                    "role": user_row.iloc[0, 2],
                                    "department": user_row.iloc[0, 3],
                                    "email": user_row.iloc[0, 4]
                                }
                                st.session_state.user_info = user_info
                                st.session_state.full_name = full_name
                                st.session_state.login_error = ""
                                st.session_state.chat_history = []
                                st.session_state.login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                update_usage_analytics()
                                st.rerun()
                        else:
                            st.session_state.login_error = "HR data not loaded. Please contact admin."
                    except Exception:
                        st.session_state.login_error = "Login failed: User not found. Please contact HR."
            if st.session_state.login_error:
                st.error(st.session_state.login_error)
                st.info("Please check your name spelling and try again. Example: Shaurya Singh\n"
                        "Make sure your department and role are correct in the HR system.")
            st.stop()

        # --- Show login time/date in main area ---
        if st.session_state.user_info and st.session_state.login_time:
            st.markdown(
                f"<div style='text-align:center;margin-bottom:1em;'>"
                f"<span style='color:#e0e6ed;font-size:1.1em;'>🕒 Logged in at: {st.session_state.login_time}</span>"
                f"</div>",
                unsafe_allow_html=True
            )

        # --- Chat Input Logic ---
        query = st.chat_input("Type your question and press Enter...") if st.session_state.user_info else None
        if query:
            # --- Role-based access check before sending to backend ---
            if not check_role_access(query, st.session_state.user_info):
                st.session_state.chat_history.append({
                    "query": query,
                    "response": "🚫 You do not have access to this information. Please contact administration."
                })
                update_usage_analytics()
            else:
                with st.spinner("Thinking..."):
                    try:
                        response = requests.post(
                            "http://localhost:8000/query",
                            json={"query": query, "user_id": st.session_state.user_info["employee_id"]},
                        )
                        response.raise_for_status()
                        result = response.json()
                        st.session_state.chat_history.append({
                            "query": query,
                            "response": result.get("response", "No response from backend.")
                        })
                        update_usage_analytics()
                    except requests.ConnectionError:
                        st.session_state.chat_history.append({
                            "query": query,
                            "response": "❌ Unable to connect to backend service at http://localhost:8000. Please ensure the backend API is running."
                        })
                        update_usage_analytics()
                    except Exception as e:
                        st.session_state.chat_history.append({
                            "query": query,
                            "response": f"Error: {str(e)}"
                        })
                        update_usage_analytics()

        if st.session_state.user_info:
            user_info = st.session_state.user_info
            st.markdown(
                f"""
                <div class="user-info-box">
                    <b>👤 {user_info['full_name']}</b> &nbsp;|&nbsp; <b>Role:</b> {user_info['role']} &nbsp;|&nbsp; <b>Dept:</b> {user_info['department']} &nbsp;|&nbsp; <b>Email:</b> {user_info['email']}
                </div>
                """, unsafe_allow_html=True
            )

            if st.session_state.chat_history:
                last = st.session_state.chat_history[-1]
                st.markdown(f'<div class="chat-bubble-user">🧑‍💼 {last["query"]}</div>', unsafe_allow_html=True)
                if last["response"].strip().lower() in [
                    "i don't know based on the available documents.",
                    "i do not know based on the available documents.",
                    "i don't know.",
                    "i do not know."
                ]:
                    st.markdown(
                        '<div class="chat-bubble-bot">🤖 Sorry, you do not have access to this information or your current role does not permit viewing this content. '
                        'If you believe you should have access, please contact your administrator or the relevant department.</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(f'<div class="chat-bubble-bot">🤖 {last["response"]}</div>', unsafe_allow_html=True)

            if st.session_state.chat_history:
                csv_data = pd.DataFrame(st.session_state.chat_history)
                st.download_button(
                    label="Download Chat History",
                    data=csv_data.to_csv(index=False).encode("utf-8"),
                    file_name="chat_history.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            st.markdown("#### 🔮 Suggestions for you:")
            role = user_info.get("role", "").lower()
            dept = user_info.get("department", "").lower()
            suggestions = []
            if "finance" in role or "finance" in dept:
                suggestions = [
                    "Show me the latest quarterly financial report.",
                    "What is our current vendor cost?",
                    "Summarize the company's revenue trends."
                ]
            elif "marketing" in role or "marketing" in dept:
                suggestions = [
                    "What are the Q4 marketing highlights?",
                    "Show me the customer acquisition cost.",
                    "Summarize our latest campaign performance."
                ]
            elif "hr" in role or "human resources" in dept:
                suggestions = [
                    "Show me the employee handbook.",
                    "How many leaves do I have left?",
                    "Who is my reporting manager?"
                ]
            elif "sales" in role or "sales" in dept:
                suggestions = [
                    "Show me my sales targets.",
                    "What is the current conversion rate?",
                    "Summarize the top performing sales regions."
                ]
            else:
                suggestions = [
                    "Show me my profile details.",
                    "What are the latest company updates?",
                    "Who can I contact for support?"
                ]
            for s in suggestions:
                st.markdown(f"- {s}")

            st.markdown("#### 📝 Your Notes")
            notes = st.text_area("Write your notes here (only visible to you):", value=st.session_state.notes, key="notes_area")
            st.download_button(
                label="Download Notes",
                data=notes.encode("utf-8"),
                file_name="user_notes.txt",
                mime="text/plain",
                use_container_width=True
            )
            st.session_state.notes = notes

# --- Footer ---
st.markdown(
    """
    <hr>
    <center>
    <span style="color:#e0e6ed;font-family:Orbitron,sans-serif;font-size:1.1rem;">
    <img src="https://th.bing.com/th/id/OIP.nukhjwUaGwnNDsCnykrM9wHaHa?w=209&h=209&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" width="30" style="vertical-align:middle;margin-right:8px;">
    Powered by <b>FinSolve AI</b> | Role-based RAG Chatbot
    <br>
    <span style="color:#cfc6e6;">FinSolve Technologies Inc &copy; 2025</span>
    </span>
    </center>
    """, unsafe_allow_html=True

)