# Chatti - AI Conversational Chatbot

Chatti is a sleek, custom-built AI assistant powered by Google's Gemini 1.5 Flash model and a Python/Flask backend. It features a fully responsive, custom-coded user interface with a seamless toggle between a high-contrast light mode and a classic dark mode.

---

## ✨ Features

-   **Conversational AI**: Powered by the Google Gemini 1.5 Flash model via the LangChain framework for intelligent and context-aware responses.
-   **Custom User Interface**: A clean, modern, and responsive chat interface built from scratch with HTML, CSS, and vanilla JavaScript.
-   **Dual Themes**: Easily switch between a unique, high-contrast light theme and a traditional dark theme to suit your preference.
-   **Extensible Framework**: Built with LangChain's ReAct agent, making it easy to add new tools and capabilities in the future.
-   **Lightweight Backend**: Uses Flask, a micro web framework for Python, to create an efficient and scalable server.

---

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **AI/LLM Framework**: LangChain, LangGraph
-   **LLM Provider**: Google Gemini
-   **Frontend**: HTML5, CSS3, JavaScript

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.8+
-   A Google API Key with the Gemini API enabled. You can get one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/ashleywyattjapan/aiChatBot.git](https://github.com/ashleywyattjapan/aiChatBot.git)
    cd aiChatBot
    ```

2.  **Create and activate a virtual environment**
    This keeps your project dependencies isolated.
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages**
    A `requirements.txt` file is recommended for managing dependencies. If you don't have one, you can install the packages directly:
    ```sh
    pip install flask langchain langchain-google-genai langgraph python-dotenv
    ```

4.  **Set up your environment variables**
    Create a file named `.env` in the root of your project directory and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    ```

5.  **Run the Flask application**
    ```sh
    python app.py
    ```

6.  **Open your browser**
    Navigate to `http://127.0.0.1:5000` to see the application live!

---

## Usage

Once the application is running, simply type your message into the input box at the bottom of the screen and press "Send" or hit Enter. The chatbot will process your message and display its response in the chat window. Use the toggle in the top-right corner to switch between light and dark modes.

---

## 📸 Screenshots


https://github.com/user-attachments/assets/bfd41fa5-b5af-4550-b525-569adade4510


| Light Mode                                               | Dark Mode                                              |
| -------------------------------------------------------- | ------------------------------------------------------ |
| ![Light Mode Screenshot](https://github.com/user-attachments/assets/502bb832-89ab-4b58-9642-57a3dee135cc) | ![Dark Mode Screenshot](https://github.com/user-attachments/assets/19095548-b43a-4b0b-babe-044e11ad38df) |


---

## 🔮 Future Improvements

-   [ ] **Theme Customization**: Add a theme palette selector to allow users to choose from multiple color schemes.
-   [ ] **Add Agent Tools**: Implement custom tools (e.g., a calculator, a web search tool) to give the agent more capabilities.
-   [ ] **Conversation History**: Implement session management to save and load chat history.
-   [ ] **Streaming Responses**: Show the AI's response token by token for a more interactive feel.

---

