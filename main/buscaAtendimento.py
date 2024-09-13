import json


class buscaAtendimento:
    def __init__(self,service):
        self.atendimentoService = service

    def buscaAtendimento(self,id):
        jsonAtendimento = self.atendimentoService.BuscaAtendimento(id)

        jsonResultado = json.dumps(jsonAtendimento, indent=4)

        return jsonResultado["id"], jsonResultado["professor"], jsonResultado["horario"], jsonResultado["periodo"],jsonResultado["sala"], jsonResultado["predio"]