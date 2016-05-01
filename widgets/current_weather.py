from kivy.factory import Factory
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from widgets.snow_conditions import SnowConditions
from main import WeatherApp

API_KEY = '787d0e1db679f03b5812253618f1481a'


class CurrentWeather(BoxLayout):
    location = ListProperty(['Fez', 'MA'])
    conditions = ObjectProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        config = WeatherApp.get_running_app().config
        temp_type = config.getdefault("General", "temp_type", "metric").lower()
        weather_template = "http://api.openweathermap.org/data/2.5/weather" \
                           "?q={},{}&units={}&appid={}"
        weather_url = weather_template.format(
            self.location[0], self.location[1], temp_type, API_KEY)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.render_conditions(data['weather'][0]['description'])
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']

    def render_conditions(self, conditions_description):
        conditions_widget = Factory.ClearConditions() \
            if "clear" in conditions_description \
            else SnowConditions() if "snow" in conditions_description \
            else Factory.UnknownConditions()
        conditions_widget.conditions = conditions_description
        self.conditions.clear_widgets()
        self.conditions.add_widget(conditions_widget)
