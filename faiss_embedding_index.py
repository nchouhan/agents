import faiss
import numpy as np

# Create a simple FAISS vector index
dimension = 512  # Vector size
index = faiss.IndexFlatL2(dimension)

# Create some dummy vectors (embeddings)
num_vectors = 10
data = np.random.rand(num_vectors, dimension).astype('float32')
index.add(data)

# Save the index
faiss.write_index(index, "vector_store.index")
