import asyncio
import websockets
from datetime import datetime


async def get_user_input(prompt):
    return await asyncio.to_thread(input, prompt)


async def connect_to_websocket():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        user = await get_user_input("Enter your name: ")
        while True:
            data = await get_user_input("Enter the message_type: ")
            message = await get_user_input("Enter your message: ")
            json_data = {"data": data, "message": message, "user": user, "time": datetime.now().time().strftime("%I:%M %p")}
            await websocket.send(f"{json_data}")
            response = await websocket.recv()
            print(response)


asyncio.run(connect_to_websocket())
