from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout

from add_location_form import AddLocationForm
from widgets.current_weather import CurrentWeather


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    locations = ObjectProperty()

    def __init__(self, **kwargs):
        super(WeatherRoot, self).__init__(**kwargs)
        self.store = JsonStore("weather_store.json")

        if self.store.exists('locations'):
            current_location = self.store.get("locations")["current_location"]
            self.show_current_weather(current_location)

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if self.current_weather is None:
            self.current_weather = CurrentWeather()
        if self.locations is None:
            self.locations = Factory.Locations()
            if self.store.exists('locations'):
                locations = self.store.get("locations")['locations']
                self.locations.locations_list.adapter.data.extend(locations)
        if location is not None:
            self.current_weather = CurrentWeather(location=location)

            adapter_data = self.locations.locations_list.adapter.data

            if location not in adapter_data:
                adapter_data.append(location)
                self.locations.locations_list._trigger_reset_populate()
                self.store.put("locations", locations=list(adapter_data),
                               current_location=location)

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
