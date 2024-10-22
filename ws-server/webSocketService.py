import asyncio
import websockets

async def handler(websocket, path):
    print("Connection established")
    number = 0
    while True:
        try:
            await websocket.send(str(number))
            number += 1
            await asyncio.sleep(1)
        except websockets.ConnectionClosed:
            print("Connection closed")
            break

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
print("Websocket server started")
asyncio.get_event_loop().run_forever()
