from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Question:

{question}
"""
)