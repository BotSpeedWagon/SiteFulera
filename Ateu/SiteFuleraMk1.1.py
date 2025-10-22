from flask import Flask, render_template, request
import aiohttp, websockets, asyncio #bibliotecas de comunicação
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("PaginaPrincipal.html")

@app.route("/pagv")
def login():
    return render_template("pagv.html")

@app.route("/pagp")
def páginaTeste():
    return render_template("pagp.html")

@app.route("/Esp", )
def homeesp():
    return render_template("controleesp.html")

@app.route("/comandoesp", methods=['POST'])
def comando_esp():
    comando = request.form["comando"]
    print(f"Comando recebido: {comando}")
    asyncio.run(EnviarCmdWs(comando))
    return f"Comando {comando} enviado ao ESP8266"
    
@app.route("/mensagemesp", methods=['POST'])
def mensagem_esp():
    mensagem = request.form["mensagem"]
    print(f"mensagem recebida: {mensagem}")
    asyncio.run(EnviarMsgWs(mensagem))
    return f"mensagem '{mensagem}' enviado ao ESP8266"

async def EnviarCmdWs(comando):
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send(comando)
        print(f"Enviando {comando} para WsServer")
async def EnviarMsgWs(mensagem):
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send(mensagem)
        print(f"Enviando a mensagem {mensagem} para o WsServer")

if __name__ == "__main__":
    app.run(debug=True)