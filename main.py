import streamlit as st

st.title("🤖 Enterprise Conversational Support Assistant (IT Services Domain Demo)")

# ---------------- SESSION STATE ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- RESPONSE FUNCTION ----------------
def generate_response(text: str) -> str:
    text = text.lower()

    # GREETING
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! Welcome to the Enterprise Support Assistant. How can I help you today?"

    # GENERAL COMPANY INFO (GENERIC)
    if "what is company" in text:
        return "It is a global IT services organization providing digital transformation, cloud, data, and AI solutions."

    if "services" in text:
        return "It offers digital transformation, cloud engineering, data analytics, AI/ML solutions, and application development services."

    if "where" in text or "location" in text:
        return "It operates globally with offices across multiple countries including India, USA, and UK."

    # CAREERS
    if "job" in text or "career" in text:
        return "You can apply for job opportunities through the official careers portal. It hires both freshers and experienced professionals."

    if "fresher" in text:
        return "Yes, it offers opportunities for freshers in software engineering, data, and support roles."

    if "interview" in text:
        return "The hiring process typically includes aptitude tests, technical rounds, coding assessments, and HR interviews."

    # TECHNOLOGY
    if "ai" in text or "artificial intelligence" in text:
        return "It provides AI-driven solutions for automation, analytics, and enterprise transformation."

    if "cloud" in text:
        return "It offers cloud migration, cloud-native development, and managed cloud services."

    if "data" in text:
        return "It works in data engineering, analytics, and business intelligence solutions."

    # SUPPORT
    if "contact" in text or "support" in text:
        return "You can reach support through the official website contact or help section."

    if "help" in text:
        return "I can assist you with information about services, careers, technology, and general queries."

   # DEFAULT RESPONSE
    return "Sorry, I am a demo Enterprise Support Assistant. I can help with services, careers, technology, and support-related queries."
# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask something about Coforge...")

# ---------------- CHAT LOGIC ----------------
if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})

    response = generate_response(user_input)

    st.session_state.chat.append({"role": "assistant", "content": response})

    st.rerun()