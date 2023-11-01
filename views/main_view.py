from views.util.ultil_view import UtilView


class MainView():

    def __init__(self):
        self.util = UtilView()
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