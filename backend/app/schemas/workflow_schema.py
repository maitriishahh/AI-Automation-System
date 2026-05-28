from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime


class WorkflowCreate(BaseModel):

    name: str

    description: str | None = None

    workflow_json: Dict[str, Any]


class WorkflowResponse(BaseModel):

    id: int

    name: str

    description: str | None = None

    workflow_json: Dict[str, Any]

    is_active: bool

    class Config:

        from_attributes = True


# ==========================================
# WORKFLOW RUN RESPONSE
# ==========================================

class WorkflowRunResponse(BaseModel):

    id: int

    workflow_name: str

    status: str

    started_at: datetime

    finished_at: datetime | None = None

    execution_results: dict | None = None

    error_message: str | None = None

    class Config:

        from_attributes = True