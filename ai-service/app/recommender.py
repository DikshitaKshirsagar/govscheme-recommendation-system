import json
from pathlib import Path

from sentence_transformers import SentenceTransformer, util


# Find the schemes.json file
BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMES_FILE = BASE_DIR / "data" / "schemes.json"


# Load the government schemes dataset
with open(SCHEMES_FILE, "r", encoding="utf-8") as file:
    schemes = json.load(file)


# Load the MiniLM AI model
print("Loading MiniLM model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("MiniLM model loaded successfully!")


# Prepare scheme descriptions
scheme_descriptions = [
    f"{scheme['name']}. {scheme['description']}. "
    f"Category: {scheme['category']}. "
    f"Keywords: {', '.join(scheme['keywords'])}"
    for scheme in schemes
]


# Generate embeddings for the schemes
scheme_embeddings = model.encode(
    scheme_descriptions,
    convert_to_tensor=True
)


def recommend_schemes(user_query: str, top_k: int = 3):
    """
    Find government schemes semantically similar to a user's query.
    """

    # Convert the user's query into an embedding
    query_embedding = model.encode(
        user_query,
        convert_to_tensor=True
    )

    # Calculate semantic similarity
    similarities = util.cos_sim(
        query_embedding,
        scheme_embeddings
    )[0]

    # Rank schemes by similarity
    ranked_indices = similarities.argsort(
        descending=True
    ).tolist()

    # Return the top matching schemes
    recommendations = []

    for index in ranked_indices[:top_k]:
        scheme = schemes[index]

        recommendations.append({
            "id": scheme["id"],
            "name": scheme["name"],
            "category": scheme["category"],
            "description": scheme["description"],
            "similarity_score": round(
                similarities[index].item(), 4
            )
        })

    return recommendations