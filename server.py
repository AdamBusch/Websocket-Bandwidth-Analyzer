import websockets
import asyncio
import sys


def on_client_connect(websocket, path):
    # Begin streaming packets to client
    print("connected!!")
    while websocket.open:
        websocket.send('1024 * 1024')


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
    server = websockets.serve(on_client_connect, ip, port)

    print("Running server on ", ip, ":", port)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()

