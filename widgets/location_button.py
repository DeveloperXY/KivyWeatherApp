from kivy.properties import ListProperty
from kivy.uix.listview import ListItemButton


class LocationButton(ListItemButton):
    location = ListProperty()
