from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton

from add_location_form import AddLocationForm


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()

    def show_current_weather(self, location):
        self.clear_widgets()

        if location is None and self.current_weather is None:
            location = "New York (US)"
        if location is not None:
            self.current_weather = Factory.CurrentWeather()
            self.current_weather.location = location

        self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())


class LocationButton(ListItemButton):
    pass


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
