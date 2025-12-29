
Python Distributed Chat Backend

Equivalent of Node.js + Express + Mongoose backend.

Components:
- FastAPI for REST APIs
- Motor (async MongoDB driver)
- Pydantic schemas
- MongoDB collections

Run:
1. pip install -r requirements.txt
2. uvicorn app.main:app --reload

APIs:
POST /chat/send
GET  /chat/room/{room}
