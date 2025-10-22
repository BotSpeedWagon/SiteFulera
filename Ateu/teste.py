from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/esp")
def teste():
    print("teste2")
    render_template("controleesp.html")

app.run(debug=True)