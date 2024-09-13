class horarioDeAtendimento:
    def __init__(self, id, nome, horario, periodo, sala, predio):
        self.id = id
        self.nome = nome
        self.horario = horario
        self.periodo = periodo
        self.sala = sala
        self.predio = predio


    def getIdProfessor(self):
        return self.id

    def getNome(self):
        return self.nome

    def getHorario(self):
        return self.horario

    def getPeriodo(self):
        return self.periodo

    def getSala(self):
        return self.sala

    def getPredio(self):
        return self.predio

    def setId(self, id):
        self.idr = id

    def setNome(self, nome):
        self.nome = nome

    def setHorarioDeAtendimento(self, horario):
        self.horario = horario

    def setPeriodo(self, periodo):
        self.periodo = periodo

    def setSala(self, sala):
        self.sala = sala

    def setPredio(self, predio):
        self.predio = predio