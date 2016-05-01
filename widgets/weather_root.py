from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from add_location_form import AddLocationForm
from widgets.current_weather import CurrentWeather


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    locations = ObjectProperty()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if location is None and self.current_weather is None:
            self.current_weather = CurrentWeather()
        if location is not None:
            self.current_weather = CurrentWeather(location=location)

        self.current_weather.update_weather()
        self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())

    def show_locations(self):
        self.clear_widgets()

        self.add_widget(self.locations)

    @staticmethod
    def format_location(location):
        return "{} ({})".format(*location)
