from fastapi import FastAPI

from backend.app.client.tmdb import get_trending
from backend.app.client.recommender import recommend

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

test_user_profile = {
    "likes": ["Better Call Saul", "The Crown"],
    "dislikes": ["superhero", "fantasy"],
    "tone": "dark, realistic",
    "max_results": 5
}

@app.get("/recommendations")
async def get_recommendations(user_profile: dict = None):
    if user_profile is None:
        user_profile = test_user_profile
    titles = get_trending()
    recommendations = recommend(titles, user_profile)
    print(recommendations)
    return {"recommendations": recommendations}
    