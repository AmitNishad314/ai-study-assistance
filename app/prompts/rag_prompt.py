from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say:

"I couldn't find the answer in the uploaded document."

------------------------
Context:

{context}

------------------------

Question:

{question}
"""
)