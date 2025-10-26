import streamlit as st
import requests
import json

st.set_page_config(page_title="Personal-ChatGPT", page_icon="💬")

st.title("💀 Personal-ChatBot")
st.write("A simple local chatbot using Ollama and Streamlit made by ragini singh")


# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **ChatGPT:** {msg['content']}")

# User input box
user_input = st.chat_input("Type your message:")

if user_input:
    # Add user message to chat
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Display user message immediately
    st.markdown(f"🧑 **You:** {user_input}")

    with st.spinner("Thinking..."):
        try:
            # Send prompt to Ollama API
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3.2:1b", "prompt": user_input, "stream": True},
                stream=True,
                timeout=30
            )

            full_reply = ""
            for line in response.iter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        full_reply += data["response"]
                    if data.get("done"):
                        break
                except json.JSONDecodeError:
                    continue

            if not full_reply.strip():
                full_reply = "(No response received from Ollama.)"

        except requests.exceptions.RequestException as e:
            full_reply = f"⚠️ Error connecting to Ollama: {e}"

    # Add response to chat
    st.session_state["messages"].append({"role": "assistant", "content": full_reply})
    
    # Rerun to show updated chat
    st.rerun()

