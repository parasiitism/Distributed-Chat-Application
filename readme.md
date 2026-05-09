# Distributed Real-Time Chat Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/System-Distributed%20Chat-7C3AED?style=for-the-badge" alt="Distributed Chat" />
  <img src="https://img.shields.io/badge/Messaging-PubSub-F97316?style=for-the-badge" alt="PubSub" />
  <img src="https://img.shields.io/badge/UI-Templates%20%2B%20JS-16A34A?style=for-the-badge" alt="UI" />
</p>

A distributed, room-based real-time chat application with a Python backend and frontend interface. The project demonstrates chat rooms, message routing, backend APIs, frontend templates, Docker support, and Pub/Sub-style design for horizontally scalable real-time communication.

![Chat Application](115279105-e6be5680-a163-11eb-9c29-cc7e4738eab0.png)

## What It Demonstrates

- Real-time chat application structure.
- Backend APIs for chat routes and message models.
- Pub/Sub boundary for distributed message delivery.
- Frontend templates and JavaScript chat behavior.
- Docker and Docker Compose backend setup.
- Separation between backend service and frontend client.

## Architecture

```mermaid
flowchart LR
    A[User Browser] --> B[Frontend App]
    B --> C[Backend API]
    C --> D[Chat Routes]
    D --> E[PubSub Layer]
    E --> F[Room Subscribers]
    C --> G[Database Layer]
    classDef client fill:#dbeafe,stroke:#2563eb,color:#1e3a8a,stroke-width:2px
    classDef backend fill:#ede9fe,stroke:#7c3aed,color:#4c1d95,stroke-width:2px
    classDef realtime fill:#ffedd5,stroke:#f97316,color:#7c2d12,stroke-width:2px
    class A,B client
    class C,D,G backend
    class E,F realtime
```

## Repository Map

```text
backend/app/main.py              Backend entry point
backend/app/routes/chat_routes.py Chat route definitions
backend/app/models/chat.py       Chat message models
backend/app/pubsub.py            Pub/Sub message boundary
backend/docker-compose.yml       Backend local infrastructure
frontend/app.py                  Frontend application
frontend/templates/              Chat UI pages
frontend/static/                 CSS and JavaScript assets
```

## Run Locally

Backend:

```powershell
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:

```powershell
cd frontend
pip install -r requirements.txt
python app.py
```

## Revision Notes

- Chat systems need message fan-out, room membership, and delivery semantics.
- A Pub/Sub boundary makes it easier to scale beyond one backend instance.
- Frontend and backend should communicate through stable APIs or websocket-style channels.

## Interview Talking Points

```text
This project is useful for explaining distributed chat fundamentals: clients connect to
a frontend, messages go through backend chat routes, and Pub/Sub fan-out allows room-based
broadcasting while keeping the service scalable.
```
