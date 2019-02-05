import pyowm


class Weather:
    owm = pyowm.OWM('58750219130143b7987aa6c46cae85f8')  # You MUST provide a valid API key

    observation = owm.weather_at_place('Rennes, Fr')
    observation_list = owm.weather_around_coords(48.117266, -1.6777926)

    def get_temperature(self, socketIo):
        socketIo.emit('ApiTemp', self, Broadcast=True)
