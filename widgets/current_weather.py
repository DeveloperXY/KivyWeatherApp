from kivy.network.urlrequest import UrlRequest
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

API_KEY = '787d0e1db679f03b5812253618f1481a'


class CurrentWeather(BoxLayout):
    location = ListProperty(['Fez', 'MA'])
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        weather_template = "http://api.openweathermap.org/data/2.5/weather" \
                           "?q={},{}&units=metric&appid={}"
        weather_url = weather_template.format(self.location[0], self.location[1], API_KEY)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
