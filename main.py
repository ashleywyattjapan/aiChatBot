from langchain_core.messages import HumanMessage #high-level framework
from langchain_google_genai import ChatGoogleGenerativeAI # CHANGED: Use this to connect to Google Gemini API
from langchain.tools import tool #use this to register tools that our ai can use.
from langgraph.prebuilt import create_react_agent #build ai agents
from dotenv import load_dotenv
import os # Import os to access environment variables

load_dotenv()

@tool 
def calculator(a: float, b: float) -> str: 
    """Useful for performing basic arithmeric calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}" #doc string/ description of tool so ai knows when to use tool 
@tool 
def say_hello(name: str) -> str: 
    """Useful for greeting user."""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today." #doc string/ description of tool so ai knows when to use tool 


def main():
    # NEW: Get the Google API key from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not found in .env file. Please make sure it's set up correctly.")
        return

    # Initialize the Google Gemini model. You can choose 'gemini-pro', 'gemini-1.5-flash', etc.
    # temperature=0 makes the model more deterministic.
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=google_api_key)

    tools = [calculator, say_hello] # if your agent needs to interact with external functions.
    agent_executor = create_react_agent(model, tools) #auto handles the model & tools

    print("Welcome! I am your AI Assistant. Type 'quit' exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:  #keep looping & allow user to keep asking questions
        user_input = input("\nYou: ").strip() #seperation from user input and agent

        if user_input.lower() == "quit": # Using .lower() for case-insensitive quit
            break

        print("\nAssistant: ", end="")
        try: # Added a try-except block to catch potential API errors
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]} #pass msgs to stream to agent
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:  #is there an agent response & if theres any messages in response
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="") #print all message content and empty str to not go to next line, agent is typing word by word instead of immediately sending the messages
            print() # Ensures the next prompt starts on a new line after the assistant's response
        except Exception as e: #  Generic error handling for unexpected issues
            print(f"An error occurred: {e}")
            print("Please check your internet connection, API key, and Gemini API quota.")


if __name__ == "__main__":
    main()