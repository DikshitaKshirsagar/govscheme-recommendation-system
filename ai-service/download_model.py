from sentence_transformers import SentenceTransformer

print("Loading the MiniLM model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")

sentences = [
    "Scholarship for college students",
    "Financial assistance for farmers"
]

embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)