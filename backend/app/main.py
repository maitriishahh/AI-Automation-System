from fastapi import FastAPI

app = FastAPI(
    title="AI Automation System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message":"AI Automation System Running"
    }

@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }