from app.db.database import (
    engine,
    Base
)

from app.models.workspace_model import Workspace
from app.models.user_model import User
from app.models.workflow_model import Workflow
from app.models.workflow_run_model import WorkflowRun
from app.models.integration_model import Integration
from app.models.log_model import Log
from app.models.lead_model import Lead


def init_db():

    Base.metadata.create_all(bind=engine)