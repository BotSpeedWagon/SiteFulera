import asyncio
import websockets

# Armazenar conexão com ESP32
esp32_conn = None

async def handler(websocket):
    global esp32_conn
    print("Nova conexão recebida!")

    try:
        async for msg in websocket:
            print(f"Mensagem recebida: {msg}")

            if msg == "esp32":
                esp32_conn = websocket
                print("ESP32 registrada!")
                await websocket.send("Servidor: ESP32 registrada com sucesso!")

            else:
                print("Comando desconhecido:", msg)

    except websockets.exceptions.ConnectionClosed:
        print("Conexão encerrada.")
        if websocket == esp32_conn:
            esp32_conn = None

async def main():
    print("Servidor WebSocket rodando na porta 8765...")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # Mantém rodando

asyncio.run(main())
