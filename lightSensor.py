import RPi.GPIO as GPIO
import time

# Initialisation des GPIOs



class LightSensor:
    broche = 14

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    def read_light(self, socketIo):
        while True:
            lightCount = 0  # intitialisation de la variable de lumière
            GPIO.setup(self.broche, GPIO.OUT)
            GPIO.output(self.broche, GPIO.LOW)
            time.sleep(0.1)  # on draine la charge du condensateur
            GPIO.setup(self.broche, GPIO.IN)
            # Tant que la broche lit ‘off’ on incrémente notre variable
            while GPIO.input(self.broche) == GPIO.LOW:
                lightCount += 1
                socketIo.emit('LightLive', lightCount, Broadcast=True)


