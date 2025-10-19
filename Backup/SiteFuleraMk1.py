from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)