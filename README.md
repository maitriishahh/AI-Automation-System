# AI Workflow Automation & CRM Platform

A scalable workflow automation platform built using FastAPI, React, PostgreSQL, and asynchronous background workers.

The platform enables businesses to automate workflows, execute integrations, monitor operations, manage leads, and orchestrate automation pipelines using a queue-based execution system.

---

# Demo Video

## Demo Video Link
[Demo Video](https://drive.google.com/file/d/1dxQWKr1tctDY9B4OaHfHSVT2FwO7z0Vu/view?usp=drive_link)

Telegram Bot Integration
<p align="center">

  <img 
    src="https://github.com/user-attachments/assets/b1e8a796-c1ca-482e-9f11-0019475cf232"
    width="150"
    height="300"
  />

</p>

Recommended demo flow:
```
Login
↓
Dashboard Overview
↓
Create Workflow
↓
Execute Gmail Workflow
↓
Queue Processing
↓
Workflow Logs
↓
Integrations
↓
Leads CRM
```
---

# Features

# Authentication System

* JWT Authentication
* Protected API Routes
* Multi-user workspace support
* Workspace-based user isolation

---

# Workflow Automation Engine

## Features

* Node-based workflow architecture
* Trigger + Action workflow model
* Workflow validation engine
* Async workflow execution
* Background worker processing
* Retry handling system
* Queue orchestration

---

# Queue-Based Execution System

The platform uses an asynchronous execution pipeline.

## Workflow
```
User Executes Workflow
↓
Workflow Added To Queue
↓
Background Worker Polling
↓
Workflow Execution Engine
↓
Integration Service Triggered
↓
Execution Logs Updated
```
This improves:

* scalability
* reliability
* fault tolerance
* async processing
* production readiness

---

# Supported Integrations

# Gmail Automation

Features:

* automated email sending
* workflow-triggered emails
* retry handling

---

# Telegram Integration

Features:

* async telegram notifications
* workflow-based message delivery
* queue-triggered execution

---

# Google Sheets Integration

Features:

* spreadsheet workflow support
* automation-ready architecture

---

# Webhook Integration

Features:

* webhook execution support
* third-party integration capability

---

# Dashboard

## Dashboard Page

Displays:

* Total workflows
* Successful runs
* Failed runs
* Success rate
* Queue monitoring
* System activity
* Workflow analytics

---

# Workflow Management

## Create Workflow

Users can:

* select workflow type
* configure automation flows
* add recipient configuration
* create workflow pipelines

---

## Workflow Analytics

Displays:

* total executions
* successful executions
* failed executions
* workflow performance
* execution success rate

---

## Workflow Logs

Displays:

* workflow history
* execution status
* start timestamps
* finish timestamps
* operational logs

---

# Leads CRM

## Features

* Lead management UI
* Lead status tracking
* Conversion monitoring
* CRM dashboard visualization

---

# Tech Stack

| Layer          | Technology              |
| -------------- | ----------------------- |
| Frontend       | React.js + Tailwind CSS |
| Backend        | FastAPI                 |
| Database       | PostgreSQL              |
| ORM            | SQLAlchemy              |
| Authentication | JWT                     |
| Queue System   | AsyncIO                 |
| API Handling   | Axios                   |
| Routing        | React Router DOM        |

---

# Project Structure

```bash id="6w3dvp"
AI Automation Platform/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── integrations/
│   │   ├── queue/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── workflows/
│   │   ├── workers/
│   │   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│
├── requirements.txt
├── package.json
└── README.md
```

---

# Installation

# Backend Setup

```bash id="v1j8ha"
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```txt id="u3m4nc"
http://localhost:8000
```

---

# Frontend Setup

```bash id="bhp7s2"
cd frontend

npm install

npm run dev
```

Frontend runs on:

```txt id="r4j7pk"
http://localhost:5173
```

---

# Environment Variables

Create a `.env` file inside backend:

```env id="s6n4fr"
DATABASE_URL=postgresql://username:password@localhost/dbname

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

EMAIL_USER=your_email@gmail.com

EMAIL_PASSWORD=your_app_password

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

TELEGRAM_CHAT_ID=your_chat_id
```

---

# Example Workflow Structure

```json id="r0f4jk"
{
  "nodes": [
    {
      "id": 1,
      "type": "trigger",
      "service": "gmail"
    },
    {
      "id": 2,
      "type": "action",
      "service": "gmail",
      "config": {
        "recipient_email": "client@gmail.com"
      }
    }
  ]
}
```

---

# Example Execution Flow
```
Create Workflow
↓
Store Workflow In Database
↓
Execute Workflow
↓
Queue Job Created
↓
Background Worker Picks Job
↓
Workflow Engine Executes Nodes
↓
Integration Triggered
↓
Execution Logs Updated
```
---

# Available Modules

* Authentication System
* Workflow Automation Engine
* Queue System
* Retry Handling
* Gmail Integration
* Telegram Integration
* Google Sheets Integration
* Webhook Support
* Workflow Analytics
* Workflow Logs
* Leads CRM
* Dashboard Monitoring

---

# Future Improvements

* Drag-and-drop workflow builder
* Workflow scheduling
* Real-time websocket monitoring
* Redis queue integration
* Docker deployment
* Kubernetes scaling
* AI workflow recommendations
* CRM backend integration

---


# Notes

The platform is fully functional in local development mode.

Cloud deployment and Dockerization were planned but not completed due to time constraints.
