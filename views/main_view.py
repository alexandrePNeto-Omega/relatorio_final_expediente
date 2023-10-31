

# from extensions.interface.interface import tk


class MainView():

    def __init__(self):

        self.__tela_config()


    def quebra_linhas(self, quantidade_cima, quantiade_baixo):
        '''Automatiza a criação dos espaços'''
        

        for espaco in range(quantidade_cima):

            print("\n")

        print("------------------------------------------------")


        for espaco in range(quantiade_baixo):

            print("\n")


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

        self.quebra_linhas(1, 1)

        print("Bem-vindo a o gerador de relatório Omega!\n")

        print("Quais das seguintes operações dejesa realiza?\n")

        print("1 - .txt\n2 - .pdf\n3 - Numvem\n")

        operaco_user = int(input(" => "))


        self.__valida_operacao([1, 2, 3], operaco_user)


        case

        self.quebra_linhas(1, 1)