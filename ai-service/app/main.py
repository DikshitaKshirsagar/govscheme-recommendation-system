from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.recommender import recommend_schemes


app = FastAPI(
    title="Government Scheme AI Service",
    description="AI-powered government scheme recommendation API",
    version="1.0.0"
)


class RecommendationRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="Describe your requirements"
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of recommendations"
    )


@app.get("/")
def home():
    return {
        "message": "Government Scheme AI Service is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "AI service is healthy"
    }


@app.post("/recommend")
def get_recommendations(request: RecommendationRequest):
    recommendations = recommend_schemes(
        user_query=request.query,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "recommendations": recommendations
    }