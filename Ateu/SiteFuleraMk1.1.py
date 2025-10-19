from flask import Flask, render_template
from aiohttp import web 
from flask_socketio import SocketIO


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
def botao():
    print('botao pressionado:')

@socketio.on("mensagem")
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")





if __name__ == "__main__":
    socketio.run(app, debug=True)