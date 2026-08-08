from embeddings.gemini_embeddings import (
    create_query_embedding
)

from prompts.rag_prompt import (
    build_rag_prompt
)

from generation.gemini_generation import (
    generate_answer
)


def answer_question(

    question,

    vector_store

):

    query_embedding = create_query_embedding(
        question
    )

    retrieved_chunks = vector_store.search(

        query_embedding,

        top_k=3

    )

    prompt = build_rag_prompt(

        question,

        retrieved_chunks

    )

    answer = generate_answer(
        prompt
    )

    return answer