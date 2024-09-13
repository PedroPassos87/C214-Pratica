import json

class Atendimento:
    def __init__(self, id, nomeProfessor, horario, periodo, sala):
        self.id = id
        self.nomeProfessor = nomeProfessor
        self.horario = horario
        self.periodo = periodo
        self.sala = sala
        self.predio = self.verificarpredio(sala)
    
    def verificarpredio(self, sala):
        if(sala >= 1 and sala <= 5):
            return 'Predio 1'
        elif(sala >= 6 and sala <= 10):
            return 'Predio 2'
        elif(sala >= 11 and sala <= 15):
            return 'Predio 3'
        elif(sala >= 16 and sala <= 20):
            return 'Predio 4'
        elif(sala >= 21 and sala <= 25):
            return 'Predio 6'
    
class buscaHorario:
    def __init__(self, service):
        self.atendimentoService = service

    def buscaAtendimento(self, id):
        jsonString = self.atendimentoService.procura_por_id(id)
        # convertendo a string em um json
        json = json.loads(jsonString)

        return json["id"], json["nomeDoProfessor"], json["horarioDeAtendimento"], json["periodo"], json["sala"], json["predio"]

    

