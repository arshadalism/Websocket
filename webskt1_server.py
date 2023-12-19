from fastapi import FastAPI, WebSocket
from datetime import datetime
import asyncio


app = FastAPI()


async def get_user_input(prompt):
    return await asyncio.to_thread(input, prompt)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print('Connection established successfully.')
    user = await get_user_input("Enter your name: ")
    while True:
        data = await websocket.receive_text()
        print(data)
        message = input("Enter the message type: ")
        response = input("Enter the reply or response: ")
        response_data = {"message": message, "reply": response, "user": user,
                         "time": datetime.now().time().strftime("%I:%M %p")}
        await websocket.send_text(f"{response_data}")
        # await asyncio.sleep(5)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
