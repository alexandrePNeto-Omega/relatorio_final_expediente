
class UtilView():

    def __init__(self):
        pass

    def quebra_linhas(self, quantidade_cima, quantiade_baixo):
        '''Automatiza a criação dos espaços'''
        
        for espaco in range(quantidade_cima):
            print("\n")

        print("------------------------------------------------")

        for espaco in range(quantiade_baixo):
            print("\n")
