from views.util.ultil_view import UtilViewConsole
from views.util.ultil_view import UtilViewDesktop

import customtkinter

from customtkinter import CTk
from customtkinter import CTkEntry
from customtkinter import CTkLabel
from customtkinter import CTkButton

#   self.window.attributes("-disabled", True)
#   self.window.state("zoomed")
#   -alpha, -transparentcolor, -disabled, -fullscreen, -toolwindow, or -topmost

class MainViewDesktop():
    def __init__(self):
        self.window = CTk()
        self.__configura_janela()
        self.__configura_layout()
        self.window.mainloop()

    def __configura_janela(self):
        self.window.title("Login")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

    def __configura_layout(self):

        #   Criar um método no util para fazer isso automático

        login_label = CTkLabel(
            master=self.window,
            text="Login"
        )
        login_label.place(x=100, y=125)

        login_user = CTkEntry(
            master = self.window,
            placeholder_text = "Informe seu usuário",
            width = 200
        )
        login_user.place(x=100, y=150)


class MainViewConsole():

    def __init__(self):
        self.util = UtilViewConsole()
        self.__tela_config()

    def __valida_operacao(self, operacoes_validas_list, operacao_usuario):

        '''Valida a operação do usuário e se entra nas requisitadas pelo sistema'''


        operador_funcao = operacao_usuario


        while True:

            if operador_funcao not in operacoes_validas_list:

                print("Favor insira um operadora válido!")

                operador_funcao = int(input(" => "))
                continue

            return

    def __tela_config(self):

        self.util.quebra_linhas(1, 1)

        print("Bem-vindo a o gerador de relatório Omega!\n")
        print("Quais das seguintes operações dejesa realiza?\n")
        print("1 - .txt\n2 - .pdf\n3 - Numvem\n")

        operaco_user = int(input(" => "))

        self.__valida_operacao([1, 2, 3], operaco_user)

        match operaco_user:
            case 1:
                from views.text_file.TextFileConsole \
                    import TextFileConsoleView

                TextFileConsoleView().main_view()
            case 2:
                None
            case 3:
                None
            case _:
                print("Operação inesperada")

        self.util.quebra_linhas(1, 1)