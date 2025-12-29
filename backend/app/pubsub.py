import redis
import threading

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

def publish(channel: str, message: str) -> None:
    """
    Publish message to Redis (non-async, safe).
    """
    redis_client.publish(channel, message)


def start_subscriber(channel: str, callback):
    """
    Start Redis subscriber in a separate thread
    to avoid blocking the event loop.
    """
    def _listen():
        pubsub = redis_client.pubsub()
        pubsub.subscribe(channel)

        for msg in pubsub.listen():
            if msg["type"] == "message":
                callback(msg["data"])

    thread = threading.Thread(target=_listen, daemon=True)
    thread.start()
