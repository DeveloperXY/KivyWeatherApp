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
        cities = [(d['name'], d['sys']['country']) for d in data['list']]
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    @staticmethod
    def args_converter(index, data_item):
        city, country = data_item
        return {'location': (city, country)}
