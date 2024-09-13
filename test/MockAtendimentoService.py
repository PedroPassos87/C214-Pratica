from main.AtendimentoService import AtendimentoService
import AtendimentosJsons

class MockAtendimentoService(AtendimentoService):
    def __init__(self):
        pass

    def Procura(self, id):
        if id == 1:
            return AtendimentosJsons.PaiDoConrado
        elif id == 2:
            return AtendimentosJsons.Chris
        elif id == 3:
            return AtendimentosJsons.Marcelo
        elif id == 4:
            return AtendimentosJsons.Joao
        elif id == 5:
            return AtendimentosJsons.Raphael
        elif id == 6:
            return AtendimentosJsons.Victoria
        elif id == 7:
            return AtendimentosJsons.Alessandra
        elif id == 8:
            return AtendimentosJsons.Vitor
        elif id == 9:
            return AtendimentosJsons.CadastroErrado
        elif id < 0:
            return AtendimentosJsons.Inexistente
        else:
            return AtendimentosJsons.Invalido