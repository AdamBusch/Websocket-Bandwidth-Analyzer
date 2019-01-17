import websockets
import asyncio
import sys


async def hello(ip, port):
    websocket = websockets.connect(ip)
    while websocket.open:
        try:
            message = await websocket.recv()
            print('Message from client: ' + str(message))
        except Exception:
            print('Client disconnected!')
            return


if __name__ == "__main__":
    ip = "ws://127.0.0.1:5000"
    port = 5000

    asyncio.get_event_loop().run_until_complete(hello(ip, port))
