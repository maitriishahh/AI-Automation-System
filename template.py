import os
import logging
from pathlib import Path

# ==========================================
# LOGGING CONFIGURATION
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s'
)

project_name = "AI-Automation-System"

# ==========================================
# FINAL PROJECT STRUCTURE
# ==========================================

list_of_files = [

    # ==========================================
    # ROOT FILES
    # ==========================================

    ".env",
    ".gitignore",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "README.md",

    # ==========================================
    # BACKEND
    # ==========================================

    "backend/__init__.py",

    # MAIN APP
    "backend/app/__init__.py",
    "backend/app/main.py",

    # ==========================================
    # API ROUTES
    # ==========================================

    "backend/app/api/__init__.py",

    "backend/app/api/auth_routes.py",
    "backend/app/api/workflow_routes.py",
    "backend/app/api/dashboard_routes.py",
    "backend/app/api/integration_routes.py",
    "backend/app/api/log_routes.py",
    "backend/app/api/webhook_routes.py",

    # ==========================================
    # AUTH
    # ==========================================

    "backend/app/auth/__init__.py",
    "backend/app/auth/jwt_handler.py",
    "backend/app/auth/hashing.py",
    "backend/app/auth/dependencies.py",

    # ==========================================
    # DATABASE
    # ==========================================

    "backend/app/db/__init__.py",
    "backend/app/db/database.py",

    # ==========================================
    # MODELS
    # ==========================================

    "backend/app/models/__init__.py",

    "backend/app/models/user_model.py",
    "backend/app/models/workspace_model.py",
    "backend/app/models/workflow_model.py",
    "backend/app/models/workflow_run_model.py",
    "backend/app/models/integration_model.py",
    "backend/app/models/log_model.py",
    "backend/app/models/lead_model.py",

    # ==========================================
    # SCHEMAS
    # ==========================================

    "backend/app/schemas/__init__.py",

    "backend/app/schemas/auth_schema.py",
    "backend/app/schemas/workflow_schema.py",
    "backend/app/schemas/integration_schema.py",
    "backend/app/schemas/dashboard_schema.py",
    "backend/app/schemas/lead_schema.py",

    # ==========================================
    # SERVICES
    # ==========================================

    "backend/app/services/__init__.py",

    "backend/app/services/auth_service.py",
    "backend/app/services/workflow_service.py",
    "backend/app/services/dashboard_service.py",
    "backend/app/services/integration_service.py",
    "backend/app/services/log_service.py",
    "backend/app/services/lead_service.py",

    # ==========================================
    # WORKFLOW ENGINE
    # ==========================================

    "backend/app/workflows/__init__.py",

    # CORE ENGINE
    "backend/app/workflows/engine.py",
    "backend/app/workflows/executor.py",
    "backend/app/workflows/conditions.py",

    # REGISTRIES
    "backend/app/workflows/action_registry.py",
    "backend/app/workflows/template_registry.py",

    # ==========================================
    # INTEGRATIONS
    # ==========================================

    "backend/app/integrations/__init__.py",

    "backend/app/integrations/gmail_service.py",
    "backend/app/integrations/google_sheets_service.py",
    "backend/app/integrations/telegram_service.py",
    "backend/app/integrations/webhook_service.py",

    # ==========================================
    # SCHEDULER + RETRIES
    # ==========================================

    "backend/app/scheduler/__init__.py",

    "backend/app/scheduler/scheduler.py",
    "backend/app/scheduler/retry_handler.py",

    # ==========================================
    # LOGGING SYSTEM
    # ==========================================

    "backend/app/logs/__init__.py",

    "backend/app/logs/workflow_logs.py",
    "backend/app/logs/audit_logs.py",
    "backend/app/logs/error_logs.py",

    # ==========================================
    # CORE CONFIG
    # ==========================================

    "backend/app/core/__init__.py",

    "backend/app/core/config.py",
    "backend/app/core/security.py",

    # ==========================================
    # UTILS
    # ==========================================

    "backend/app/utils/__init__.py",

    "backend/app/utils/logger.py",
    "backend/app/utils/helpers.py",
    "backend/app/utils/retry.py",

    # ==========================================
    # FRONTEND
    # ==========================================

    "frontend/package.json",
    "frontend/vite.config.js",

    # PUBLIC
    "frontend/public/.gitkeep",

    # SRC
    "frontend/src/main.jsx",
    "frontend/src/App.jsx",
    "frontend/src/index.css",

    # ==========================================
    # FRONTEND COMPONENTS
    # ==========================================

    "frontend/src/components/.gitkeep",

    "frontend/src/components/Navbar.jsx",
    "frontend/src/components/Sidebar.jsx",

    "frontend/src/components/WorkflowCard.jsx",
    "frontend/src/components/StatsCard.jsx",
    "frontend/src/components/LogTable.jsx",

    # ==========================================
    # FRONTEND PAGES
    # ==========================================

    "frontend/src/pages/Login.jsx",
    "frontend/src/pages/Dashboard.jsx",
    "frontend/src/pages/Workflows.jsx",
    "frontend/src/pages/Integrations.jsx",
    "frontend/src/pages/Logs.jsx",

    # ==========================================
    # FRONTEND SERVICES
    # ==========================================

    "frontend/src/services/api.js",

    # ==========================================
    # DOCS
    # ==========================================

    "docs/architecture.md",
    "docs/api_documentation.md"
]

# ==========================================
# CREATE FILES & FOLDERS
# ==========================================

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

        logging.info(
            f"Creating directory: {filedir} for file: {filename}"
        )

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")

print("\nProject structure created successfully!")