from fastapi import APIRouter, HTTPException
from app.database import db
from app.models.chat import Chat
from app.pubsub import publish

router = APIRouter()


@router.post("/send")
async def send_chat(chat: Chat):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not initialized")

    # Persist message
    await db.chats.insert_one(chat.dict())

    # Broadcast via Redis so all nodes receive it
    publish(chat.room, f"{chat.user}: {chat.data}")

    return {"status": "message stored and broadcast"}


@router.get("/room/{room}")
async def get_room_messages(room: str, limit: int = 50):
    if db is None:
        raise HTTPException(status_code=500, detail="Database not initialized")

    cursor = (
        db.chats
        .find({"room": room})
        .sort("time", -1)
        .limit(limit)
    )

    messages = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        messages.append(doc)

    return list(reversed(messages))
