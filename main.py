from kivy.app import App

import widgets.weather_root
from widgets.location_button import LocationButton


class WeatherApp(App):
    pass


def args_converter(index, data_item):
    city, country = data_item
    return {'location': (city, country)}


if __name__ == '__main__':
    WeatherApp().run()
