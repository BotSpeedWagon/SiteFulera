from flask import Flask, render_template, request
import asyncio
import websockets

app = Flask(__name__)

# Função que envia mensagem ao servidor_ws.py
async def enviar_para_esp32(msg):
    try:
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send(msg)
            print(f"Comando '{msg}' enviado ao servidor WebSocket")
    except Exception as e:
        print("Erro ao enviar:", e)

@app.route("/")
def home():
    return render_template("controle.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    comando = request.form["comando"]
    asyncio.run(enviar_para_esp32(comando))
    return "Comando enviado!"

if __name__ == "__main__":
    app.run(debug=True)
