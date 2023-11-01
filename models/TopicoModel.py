TOPICO_CONSOLE_LIST = [
    "1 - ROTINA DIARIA",
    "2 - SALESFORCE",
    "3 - MILVUS"
]

TOPICO_LIST = [
    "ROTINA DIARIA",
    "SALESFORCE",
    "MILVUS"
]

class TopicoModel():
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
