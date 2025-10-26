 Personal-ChatBot:[Ollama3.2:1b]

This project is a fast, web-based chat application that works like a local version of ChatGPT. It uses Ollama to run a powerful Large Language Model (LLM) directly on your computer, ensuring speed and privacy.

✨ Quick Summary
What it is: A web application built with Streamlit.
How it works: It connects to the Ollama service running in the background.
Model Used: llama3.2:1b (The specific model required by the code).

🚀 Getting Started
Follow these three simple steps to set up and run the bot.

1. Prerequisite: Set up Ollama
You must have the Ollama application running.
Download Model: Open your terminal and run the command to download the model used in the app:
ollama pull llama3.2:1b


2. Install Project Files
Clone the Repository:
git clone [YOUR_GITHUB_REPO_URL]
cd [YOUR_PROJECT_FOLDER_NAME]

Activate Environment: (Assuming your environment is named venv)
.\venv\Scripts\Activate.ps1  # For Windows PowerShell
Install Libraries:
pip install -r requirements.txt


3. Run the Chatbot
Make sure Ollama is running and the model is loaded.
streamlit run app.py
The application will open automatically in your web browser at http://localhost:8501.

📚 Tech Details
Frontend: Streamlit
Backend/Model: Ollama LLM
Libraries: streamlit, requests

👨‍💻 Author
Developed by [Ragini Singh]
