# app.py
from flask import Flask, render_template, request, jsonify
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os
import asyncio #For async handling if needed, though Flask usually handles sync.

load_dotenv()

app = Flask(__name__)

# Initialize the Gemini model globally so it's only done once

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("Error: GOOGLE_API_KEY not found in .env file. Please make sure it's set up correctly.")

llm_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=google_api_key)
tools = []
# The agent_executor needs to be initialized here as well
agent_executor = create_react_agent(llm_model, tools)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"response": "No message received."}), 400

    try:
        # LangGraph's .stream() returns an async generator.
        # We need to run it in a synchronous context for Flask.
        # This is a simplified way; for complex async, use an async Flask setup.
        full_response_content = ""
        # Create a simple list to hold messages from the agent stream
        messages_from_agent = []

        # Run the async stream in a synchronous context
        
        # NOTE: For `agent_executor.stream`, it's generally an async generator.
    

        # iterating directly as Langchain runnables designed for both.
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    full_response_content += message.content

        return jsonify({"response": full_response_content})

    except Exception as e:
        print(f"Error during chatbot interaction: {e}")
        return jsonify({"response": f"An error occurred: {e}. Please check the server logs."}), 500

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for auto-reloading on code changes