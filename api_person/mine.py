from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/person") #aquí especificamos la ruta para el endpoint.
def handle_person(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    return "Hello Person!" #aquí especificamos el string que queremos responder al cliente.

app.run(host='0.0.0.0')
