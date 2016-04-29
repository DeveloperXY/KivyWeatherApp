from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

API_KEY = '787d0e1db679f03b5812253618f1481a'


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&appid={}"
        search_url = search_template.format(self.search_input.text, API_KEY)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
