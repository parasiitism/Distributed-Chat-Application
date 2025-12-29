
from datetime import datetime
from pydantic import BaseModel

class Chat(BaseModel):
    time: datetime = datetime.utcnow()
    user: str
    room: str
    data: str
    type: str
    broadcast: int
    unicast: bool
    toUser: str | None = None
