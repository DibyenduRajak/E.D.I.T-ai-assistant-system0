import asyncio
from core.brain import process_input
from core.router import route
from voice.wake_listener import listen
from voice.speak import speak
from api.server import broadcast

async def main():
    while True:
        await broadcast("Listening...")
        user = listen()

        await broadcast(f"You: {user}")
        await broadcast("Thinking...")

        decision = process_input(user)
        result = route(decision)

        await broadcast(f"E.D.I.T: {result}")
        speak(result)

asyncio.run(main())
