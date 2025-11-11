#!/usr/bin/env python
import asyncio
from websockets.asyncio.server import serve


clientes = {} 
conexoes = set()

async def handle_client(websocket):
    print("Novo cliente conectado!")

    try:





        identificador = await websocket.recv()
        clientes[identificador] = websocket
        conexoes.add(websocket)
        print(f"Cliente identificado como: {identificador}")

        async for mensagem in websocket:

            if mensagem.startswith("FRAME:"):
                for nome, conn in clientes.items():
                    if nome != "ESP32":
                        await conn.send(mensagem)
                continue

            print(f"{identificador} enviou: {mensagem}")






            if identificador == "FLASK" and "ESP32" in clientes:
                try:
                    await clientes["ESP32"].send(mensagem)
                    print(f"→ Repassado para ESP32: {mensagem}")
                except:
                    print("Erro ao enviar para ESP32")

    
            elif identificador == "ESP32":
                for nome, conn in clientes.items():
                    if nome != "ESP32":
                        try:
                            await conn.send(mensagem)
                            print(f"→ Repassado para {nome}: {mensagem}")
                        except:
                            print(f"Erro ao enviar para {nome}")


  
            elif identificador not in ["FLASK", "ESP32"]:
                if "FLASK" in clientes:
                    try:
                        await clientes["FLASK"].send(mensagem)
                        print(f"→ {identificador} → FLASK: {mensagem}")
                    except:
                        print("Erro ao enviar para FLASK")
    except Exception as e:
        print(f"Erro com {identificador}: {e}")

    finally:
        conexoes.discard(websocket)
        for nome, conn in list(clientes.items()):
            if conn == websocket:
                del clientes[nome]
                print(f"{nome} desconectado.")

async def main():
    async with serve(handle_client, "0.0.0.0", 8765):
        print("Servidor WebSocket rodando em ws://0.0.0.0:8765")
        await asyncio.Future() 


if __name__ == "__main__":
    asyncio.run(main())