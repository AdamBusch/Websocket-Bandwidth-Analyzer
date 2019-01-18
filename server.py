import websockets
import asyncio
import sys


def sizeof_fmt(num, suffix='B'):
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

async def on_client_connect(websocket, path):
    # Begin streaming packets to client
    msg = b'\0' * int(1E6)
    size = sizeof_fmt(sys.getsizeof(msg))
    print("Streaming data packets of size", size)
    
    while websocket.open:
        await websocket.send(msg)


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
    server = websockets.serve(on_client_connect, ip, port)

    print("Running server on ", ip, ":", port)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()

