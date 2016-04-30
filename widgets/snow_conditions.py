import random

from kivy.clock import Clock
from kivy.graphics import Color, Ellipse

from widgets.conditions import Conditions


class SnowConditions(Conditions):
    FLAKE_SIZE = 5
    NUM_FLAKES = 60
    FLAKE_AREA = FLAKE_SIZE * NUM_FLAKES
    FLAKE_INTERVAL = 1.0 / 30.0

    def __init__(self, **kwargs):
        super(SnowConditions, self).__init__(**kwargs)
        self.flakes = [[x * self.FLAKE_SIZE, 0] for x in range(self.NUM_FLAKES)]
        Clock.schedule_interval(self.update_flakes, self.FLAKE_INTERVAL)

    def update_flakes(self, time):
        for f in self.flakes:
            f[0] += random.choice([-1, 1])
            f[1] -= random.randint(0, self.FLAKE_SIZE)
            if f[1] <= 0:
                f[1] = random.randint(0, int(self.height))

        self.canvas.before.clear()
        with self.canvas.before:
            widget_x = self.center_x - self.FLAKE_AREA / 2
            widget_y = self.pos[1]
            for x_flake, y_flake in self.flakes:
                x = widget_x + x_flake
                y = widget_y + y_flake
                Color(0.9, 0.9, 1.0)
                Ellipse(pos=(x, y), size=(self.FLAKE_SIZE, self.FLAKE_SIZE))
