from embeddings.gemini_embeddings import (
    create_query_embedding
)

from vector_store.faiss_store import (
    FaissVectorStore
)


store = FaissVectorStore()

store.load()


while True:

    query = input(
        "\nQuestion: "
    ).strip()


    if query.lower() == "exit":
        break


    if not query:
        continue


    query_embedding = (
        create_query_embedding(query)
    )


    results = store.search(
        query_embedding,
        top_k=3
    )


    print("\nRelevant Chunks:\n")


    for number, result in enumerate(
        results,
        start=1
    ):

        print(
            f"{number}. "
            f"Page {result['metadata']['page']} "
            f"(score={result['score']:.4f})"
        )

        print(
            result["text"][:500]
        )

        print()