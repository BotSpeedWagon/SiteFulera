from flask import Flask, render_template, request, Response, jsonify
import websockets, asyncio
import cv2
app = Flask(__name__)
cap = cv2.VideoCapture(1)

@app.route("/")
def home():
    return render_template("PaginaPrincipal.html")

@app.route("/pagv")
def login():
    return render_template("pagv.html")

@app.route("/pagp")
def páginaTeste():
    return render_template("pagp.html")

@app.route("/teste")
def testeslasla():
    return render_template("teste.html")

@app.route("/Esp")
def homeesp():
    return render_template("controleesp.html")

@app.route("/comandoesp", methods=['POST'])
def comando_esp():
    comando = request.form["comando"]
    print(f"Comando recebido: {comando}")
    asyncio.run(EnviarCmdWs(comando))
    return f"Comando {comando} enviado ao ESP32"

@app.route("/mensagemesp", methods=['POST'])
def mensagem_esp():
    mensagem = request.form["mensagem"]
    print(f"mensagem recebida: {mensagem}")
    asyncio.run(EnviarMsgWs(mensagem))
    return f"mensagem '{mensagem}' enviado ao Esp"

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#FUNÇÕES ATIVAS
def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            continue
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

async def EnviarCmdWs(comando):
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("FLASK")  # se identifica primeiro
        await ws.send(comando)
        print(f"Enviado '{comando}' para servidor WS")

async def EnviarMsgWs(mensagem):
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("FLASK")  # <--- adicionar esta linha
        await ws.send(mensagem)
        print(f"Enviando a mensagem {mensagem} para o WsServer")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)