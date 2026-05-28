import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.workflow_routes import router as workflow_router
from app.api.integration_routes import router as integration_router
from app.api.webhook_routes import router as webhook_router
from app.api.dashboard_routes import router as dashboard_router
from app.db.init_db import init_db

from app.queue.worker import start_worker

import app.scheduler.scheduled_jobs

@asynccontextmanager
async def lifespan(app: FastAPI):

    init_db()

    asyncio.create_task(
        start_worker()
    )

    print("Background worker started...")

    yield

    print("Application shutting down...")

app = FastAPI(
    title="AI Automation System",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(workflow_router)
app.include_router(integration_router)
app.include_router(webhook_router)
app.include_router(dashboard_router)

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