import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.routes.chat_routes import router as chat_router
from app.pubsub import publish, start_subscriber
from app.websocket_manager import ConnectionManager

app = FastAPI(title="Distributed Chat Backend")

manager = ConnectionManager()

# ---------- REST ROUTES ----------
app.include_router(chat_router, prefix="/chat")


# ---------- WEBSOCKET ----------
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(username, websocket)

    try:
        while True:
            message = await websocket.receive_text()
            publish("chat_room", f"{username}: {message}")
    except WebSocketDisconnect:
        manager.disconnect(username)


# ---------- REDIS SUBSCRIBER ----------
@app.on_event("startup")
def start_redis_listener():
    start_subscriber(
        "chat_room",
        lambda msg: asyncio.create_task(manager.broadcast(msg))
    )
