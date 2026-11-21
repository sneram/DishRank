from fastapi import FastAPI

app = FastAPI(
    title="DishRank API",
    description="AI-powered restaurant dish discovery platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DishRank API!",
        "status": "Running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }