from abc import ABC, abstractmethod

class AtendimentoService(ABC):

    @abstractmethod
    def procura_por_id(self):
        pass
