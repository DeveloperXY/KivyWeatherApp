from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory

API_KEY = '787d0e1db679f03b5812253618f1481a'


class WeatherRoot(BoxLayout):
    def show_current_weather(self, location):
        self.clear_widgets()
        current_weather = Factory.CurrentWeather()
        current_weather.location = location
        self.add_widget(current_weather)


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&appid={}"
        search_url = search_template.format(self.search_input.text, API_KEY)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        # self.search_results.item_strings = cities
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()


class LocationButton(ListItemButton):
    pass


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
