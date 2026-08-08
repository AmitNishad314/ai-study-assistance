from embeddings.gemini_embeddings import create_embedding


text = "Gradient descent minimizes the loss function."


embedding = create_embedding(text)


print("Embedding:")

print(embedding[:10])


print("\nDimensions:")

print(len(embedding))