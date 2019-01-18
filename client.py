import websockets
import asyncio
import sys
import time


def sizeof_fmt(num, suffix='B'):
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

async def connectServer(ip, port):
    async with websockets.connect(ip) as websocket:

        incoming_bytes = 0
        start_time = time.time()

        while True:
            data = await websocket.recv()
            incoming_bytes += sys.getsizeof(data)

            time_elapsed = time.time() - start_time
            if time_elapsed >= 0.5:
                size = sizeof_fmt(incoming_bytes / time_elapsed)
                print(size)
                incoming_bytes = 0
                start_time = time.time()

if __name__ == "__main__":
    ip = "ws://127.0.0.1:5000"
    port = 5000

    asyncio.get_event_loop().run_until_complete(connectServer(ip, port))
