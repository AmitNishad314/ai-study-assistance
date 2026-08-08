from embeddings.gemini_embeddings import (
    create_query_embedding
)

from retrieval.similarity import (
    cosine_similarity
)


def semantic_search(
    query,
    embedded_chunks,
    top_k=3
):

    query_embedding = (
        create_query_embedding(query)
    )


    results = []


    for chunk in embedded_chunks:

        score = cosine_similarity(
            query_embedding,
            chunk["embedding"]
        )


        results.append({

            "score": score,

            "text": chunk["text"],

            "metadata": chunk["metadata"]

        })


    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    return results[:top_k]