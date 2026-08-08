from commands import HELP_TEXT, ABOUT_TEXT
from gemini_client import stream_response

def print_header():
    print("=" * 50)
    print("AI STUDY ASSISTANT")
    print("=" * 50)
    print("Ask me anything.")
    print("Type 'exit' to quit.\n")

def main():
    
    print_header()
    previous_interaction_id = None

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        
        if not user_input:
            print("Please enter a question or type 'exit' to quit.")
            continue
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if user_input.lower() == '/help':
            print(HELP_TEXT)
            continue
        
        if user_input.lower() == '/about':
            print(ABOUT_TEXT)
            continue
        
        if user_input.lower() == '/reset':
            previous_interaction_id = None
            print("Conversation reset. You can start a new conversation now.")
            continue
        
        #----------------------------
        # LLM
        #----------------------------
        print("\nAI: ", end="", flush=True)
        
        try:
            previous_interaction_id = stream_response(user_input, previous_interaction_id)
            
        except Exception as e:
            print(f"\nError: {e}")


        
if __name__ == "__main__":
    main()
    
    