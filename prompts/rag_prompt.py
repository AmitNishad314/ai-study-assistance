def build_rag_prompt(question, retrieved_chunks):

    context = ""
    pages=set()

    for chunk in retrieved_chunks:

        page = chunk["metadata"]["page_number"]
        pages.add(page)

        context += (
            f"\n[Page {page}]\n"
            f"{chunk['text']}\n"
        )
    pages_text = ", ".join(str(page) for page in sorted(pages))

    prompt = f"""
You are an AI Study Assistant.

The user has uploaded a PDF.

If the user is greeting you (such as "hello", "hi", "thanks", etc.),
respond naturally without saying the information is missing from the document.

For questions about the uploaded document:
- Answer ONLY using the provided context.
- Do NOT make up information.
- If the answer is not present in the context, reply exactly:
"I couldn't find this information in the uploaded document."

--------------------
CONTEXT
--------------------

{context}

--------------------
QUESTION
--------------------

{question}

--------------------
ANSWER
--------------------

Provide a clear, concise answer.

If you used the context, end your answer with:

Source: Page(s) {pages_text}
"""

    return prompt