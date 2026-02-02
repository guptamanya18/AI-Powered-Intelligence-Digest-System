import faiss
import numpy as np
import os
import pickle

VECTOR_DIM = 4096  # LLaMA3 embedding size
INDEX_PATH = "data/faiss.index"
META_PATH = "data/faiss_meta.pkl"

class VectorStore:

    def __init__(self):
        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(VECTOR_DIM)
            self.metadata = []

    def add(self, vector: list[float], meta: dict):
        self.index.add(np.array([vector]).astype("float32"))
        self.metadata.append(meta)
        self._persist()

    def search(self, vector: list[float], k=1):
        if self.index.ntotal == 0:
            return None, None

        distances, indices = self.index.search(
            np.array([vector]).astype("float32"), k
        )

        return distances[0][0], self.metadata[indices[0][0]]

    def _persist(self):
        faiss.write_index(self.index, INDEX_PATH)
        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadata, f)
