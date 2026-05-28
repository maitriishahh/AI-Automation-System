from fastapi import FastAPI

from app.api.auth_routes import router as auth_router
from app.api.workflow_routes import router as workflow_router

from app.db.init_db import init_db

from app.api.integration_routes import router as integration_router

app = FastAPI(
    title="AI Automation System",
    version="1.0.0"
)

init_db()

app.include_router(auth_router)
app.include_router(workflow_router)
app.include_router(integration_router)
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