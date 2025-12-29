from motor.motor_asyncio import AsyncIOMotorClient

# Docker service name = hostname
MONGO_URI = "mongodb://mongodb:27017"

client: AsyncIOMotorClient | None = None
db = None


def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.chatdb


def close_mongo_connection():
    if client:
        client.close()
