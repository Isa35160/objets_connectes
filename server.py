import threading

from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send, emit

from lightSensor import LightSensor
from temperatureSensor import TemperatureSensor
app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

# définition de nos objets


tempSens = TemperatureSensor()
lightSens = LightSensor()

# threading sur le thermomètre et le capteur de lumière
temp = threading.Thread(target=tempSens.readTempLive, args=(socketio,))
lightSens = threading.Thread(target=lightSens.read_light, args=(socketio,))

lightSens.start()
temp.start()

