#!/usr/bin/env python
import asyncio
from websockets.asyncio.server import serve


async def receberComando(webscoket):
    comando = await webscoket.recv()
    print(f"Recebido o comando {comando}")


async def main():
    async with serve(receberComando, "", 8765) as server:
        await server.serve_forever()
asyncio.run(main())