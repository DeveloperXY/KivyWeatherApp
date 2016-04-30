from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from add_location_form import AddLocationForm
from widgets.current_weather import CurrentWeather


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if location is None and self.current_weather is None:
            location = ("New York", "US")
        if location is not None:
            self.current_weather = CurrentWeather(location=location)

        self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())

    @staticmethod
    def format_location(location):
        return "{} ({})".format(location[0], location[1])
