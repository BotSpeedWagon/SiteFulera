#Vulgo main.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import websockets
import asyncio

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LegoBatmanFulera'
socketio.init_app(app)

@app.route("/")
def home():
    return render_template("PaginaPrincipal.html")

@app.route("/initial")
def login():
    return render_template("initial.html")

@app.route("/testeP")
def páginaTeste():
    return render_template("pagp.html")

@app.route("/testeV")
def páginaTesteV():
    return render_template("pagtestv.html")

@app.route("/Esp")
def homeesp():
    return render_template("controleesp.html")

@socketio.on('comando')
def botao(comando):
    if 'velocidade:' not in comando:
        print(f'botao pressionado: {comando}')
        comando = request.form["comando"]
        asyncio.run(enviar_comando_ws(comando))

@socketio.on("mensagem")
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")



if __name__ == "__main__":
    socketio.run(app, debug=True)



async def enviar_comando_ws(comando):
    try:
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send(comando)
            print(f"Enviado ao WS: {comando}")
            resposta = await ws.recv()
            print(f"Resposta do WS: {resposta}")
    except Exception as e:
        print("Erro ao conectar com WebSocket:", e)