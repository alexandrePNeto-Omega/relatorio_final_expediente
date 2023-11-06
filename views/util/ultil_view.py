import customtkinter

class UtilViewDesktop():

    def __init__(self):
        pass

    def retorna_config_user(self):
        config = open("user.conf", "r")
        return config.readline()
    
    def grava_config_user(self, new_config):
        config = open("user.conf", "w")
        config.write(new_config)

    def botao_troca_tema(self):
        if self.retorna_config_user() == "dark":
            customtkinter.set_appearance_mode("light")
            self.grava_config_user("light")
            return
        
        customtkinter.set_appearance_mode("dark")
        self.grava_config_user("dark")
        return

class UtilViewConsole():

    def __init__(self):
        pass

    def quebra_linhas(self, quantidade_cima, quantiade_baixo):
        '''Automatiza a criação dos espaços'''
        
        for espaco in range(quantidade_cima):
            print("\n")

        print("------------------------------------------------")

        for espaco in range(quantiade_baixo):
            print("\n")
