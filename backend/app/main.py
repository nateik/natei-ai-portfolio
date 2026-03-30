from fastapi import FastAPI

app = FastAPI(title="AI Portfolio API")


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "backend"}
