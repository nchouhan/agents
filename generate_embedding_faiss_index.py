import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize a text embedding model (SBERT)
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small & efficient model

# Sample text documents
documents = [
    "The best coffee shop in San Francisco is Blue Bottle.",
    "Starbucks has a variety of coffee blends.",
    "Today's weather in SF is sunny with a chance of rain.",
    "For the best espresso, visit Philz Coffee.",
    "Cold brew coffee is great for hot weather.",
]

# Convert text documents into numerical embeddings
embeddings = model.encode(documents)

# Convert embeddings to a NumPy float32 array
embeddings = np.array(embeddings, dtype='float32')

# Initialize FAISS index (L2 distance)
dimension = embeddings.shape[1]  # Size of embedding vector
index = faiss.IndexFlatL2(dimension)

# Add embeddings to FAISS index
index.add(embeddings)

# Save the FAISS index
faiss.write_index(index, "vector_store.index")

print(f"Stored {len(documents)} documents in FAISS!")
