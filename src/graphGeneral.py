import geobr
import matplotlib.pyplot as plt
import pandas as pd


# %matplotlib inline

class BrazilGraph:

    def __init__(self):
        self.states = geobr.read_state(year=2020)
        print(geobr.list_geobr())

        def show_map():
            fig, ax = plt.subplots(figsize=(15, 15), dpi=300)
            self.states.plot(facecolor="#2D3E50", edgecolor="#FEBF57", ax=ax)
            ax.set_title("States", fontsize=20)
            ax.axis("off")
            plt.show()

        show_map()
