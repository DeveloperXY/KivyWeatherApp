from kivy.app import App

import widgets.weather_root
from widgets.location_button import LocationButton


class WeatherApp(App):
    def build_config(self, config):
        config.setdefaults('General', {'temp_type': "Metric"})

    def build_settings(self, settings):
        settings.add_json_panel("Weather Settings", self.config,
                                data="""
                                [
                                    {
                                        "type": "options",
                                        "title": "Temperature System",
                                        "section": "General",
                                        "key": "temp_type",
                                        "options": ["Metric", "Imperial"]
                                    }
                                ]
                                """)


def args_converter(index, data_item):
    city, country = data_item
    return {'location': (city, country)}


if __name__ == '__main__':
    WeatherApp().run()
