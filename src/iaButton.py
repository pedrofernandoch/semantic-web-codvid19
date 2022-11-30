import pygame_widgets
from pygame_widgets.button import Button
from graphGeneral import BrazilGraph


class IaButton:

    def __init__(self, scr, name, pos):
        self.pos = pos
        self.name = name
        self.calc = len(name) * 10
        self.button = Button(
            scr,
            (600 // 2) - self.calc / 2,  # x position
            (600 // 2) + (pos * 40) + (pos * 10),  # y position = middle + pos * button height + (pos * gap)
            self.calc,  # width
            40,  # height
            text=name,
            fontSize=20,
            textColour=(255, 255, 255),
            margin=20,
            inactiveColour=(72, 72, 72),
            radius=20,
            onClick=lambda: search_choice(self)
        )

        #
        #
        #
        # BUTTOM SEARCH REDIRECT #
        def search_choice(self):
            def graph_general():
                print("graph general")
                BrazilGraph()

            def graph_per_area():
                print("graph per area")

            # dictionary with methods related to buttons
            dict = {
                0: graph_general,
                1: graph_per_area,
            }

            dict.get(self.pos)()

        # draw buttons on screen
        #self.button.draw()


