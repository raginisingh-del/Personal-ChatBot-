Personal-ChatBot — Chatbot using Ollama + Streamlit

Personal-ChatBot is a lightweight, privacy-friendly local chatbot built with Streamlit and powered by Ollama models like deepseek-r1:1.5b. It supports multiple chat sessions, live response streaming, and even shows the model’s hidden thought process (using <think> tags, if supported by the model).

🚀 Features
✅ Multiple Chat Sessions – Create, switch, and resume chats easily from the sidebar (requires code implementation beyond the base template).
✅ Live Streaming Output – Watch the bot respond in real time.
✅ Hidden Thought Display – View the model’s internal reasoning in an expandable “🧠 Thoughts” section (if model supports <think> tags).
✅ Local Privacy – Works completely offline using Ollama — no external API calls.
✅ Clean Math Rendering – Converts LaTeX-style symbols (like \frac, \times, etc.) into readable Unicode (requires additional libraries/logic).
✅ Session Persistence – Each chat session is uniquely saved with timestamps.

🧠 How It Works
Section
Description
Frontend
Streamlit provides a simple and elegant web interface.
Ollama runs a local model (e.g., deepseek-r1:1.5b) via the REST API endpoint http://localhost:11434/api/generate.
Streaming Responses
The chatbot listens to a streaming response from Ollama and renders each chunk live.
Session Management
Chats are stored in st.session_state for persistence, including both visible messages and hidden thoughts.

⚙️ Installation
1️⃣ Install Ollama
Download and install Ollama from the official website.
2️⃣ Pull a model
Pull the recommended model or the model currently configured in your app.py:
ollama pull deepseek-r1:1.5b

You can replace this with any compatible model (like llama3, mistral, etc.).
3️⃣ Install dependencies
Navigate to your project folder, activate your virtual environment (.\venv\Scripts\Activate.ps1), and install:
pip install streamlit requests

🧩 Run the App
Save the code as app.py, then start the Streamlit server:
streamlit run app.py

Make sure Ollama is running in the background (it starts automatically when you run a model).
Then open the app in your browser at: 👉 http://localhost:8501

💡 Usage
Type your message in the chat input at the bottom.
The chatbot will stream its answer live.
Click on 🧠 Model’s Thought Process to see what the model “thought” before answering.
Start a new chat or revisit old ones using the sidebar.

🧑‍💻 Author
👤 [Ragini Singh] | Built with  using Python, Streamlit, and Ollama.

📜 License
This project is open-source under the MIT License — feel free to modify and improve it.ed by [Ragini Singh]
