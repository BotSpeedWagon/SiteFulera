import asyncio
import websockets

async def enviar_comando_ws(comando):
    try:
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send(comando)
            print(f"Enviado para WS: {comando}")
            # opcional: receber resposta
            resposta = await ws.recv()
            print(f"Resposta do WS: {resposta}")
    except Exception as e:
        print("Erro ao conectar com WebSocket:", e)
