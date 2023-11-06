import os
import time

from models.StatusModel import STATUS
from models.TopicoModel import TOPICO_CONSOLE_LIST

from views.util.ultil_view import UtilViewConsole

class TextFileConsoleView():
    def __init__(self):
        self.util = UtilViewConsole()

    def main_view(self):

        os.system("cls")

        operacao_check_dict = {}        

        while True:
            print("\n+------------- Arquivo Console --------------+\n")

            if self.verifica_topicos_preenchidos(operacao_check_dict):
                break

            print("Informe quais dos topicos dejesa preencher: " + ", ".join(TOPICO_CONSOLE_LIST))

            operacao_user = input(" => ")

            self.util.quebra_linhas(0, 0)

            if operacao_user not in self.pega_valor_topico_list():
                print("Tópico não registrado, tente novamente amigão! Aguarde 1.5 segundos.")
                time.sleep(1.5)
                os.system("cls")
                continue
            
            if operacao_check_dict.get(operacao_user):
                print("Tópico já preenchido anteriormente! Aguarde 1.5 segundos.")
                #### TODO MOCK: Colocar opções para editar e visualizar como ele está
                time.sleep(1.5)
                os.system("cls")
                continue
            
            self.monta_linhas_registro(operacao_user)

            operacao_check_dict[operacao_user] = True
            print("Tópico preenchido com sucesso!")
            time.sleep(1.5)
            os.system("cls")
        
        print("Deu boa!")

    def verifica_topicos_preenchidos(self, operacao_dict):
        if len([operacao for operacao in operacao_dict.keys()]) == len(TOPICO_CONSOLE_LIST):
            print("Todos os tópicos já preechidos")
            time.sleep(1.5)
            os.system("cls")
            return True
        return False

    def monta_linhas_registro(self, topico):
        pass

    def pega_valor_topico_list(self):
        return [topico.strip().split("-")[0].strip() for topico in TOPICO_CONSOLE_LIST]