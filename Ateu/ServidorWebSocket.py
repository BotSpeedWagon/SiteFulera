
import asyncio
import websockets

async def handler(websocket):
    print("Cliente conectado ao WS!")
    try:
        async for mensagem in websocket:
            print(f"Mensagem recebida pelo WS: {mensagem}")
            await websocket.send(f"Recebido: {mensagem}") 
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectou!")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Servidor WebSocket rodando na porta 8765...")
        await asyncio.Future()  

asyncio.run(main())
