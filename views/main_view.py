
from extensions.interface.interface import tk

from tkinter import *

class MainView():
    def __init__(self):
        self.__tela_config()

    def __tela_config(self):
        main_view = tk()
        main_view.title("Teste 2")
        main_view.resizable(width = 1, height = 1)
        main_view.mainloop()