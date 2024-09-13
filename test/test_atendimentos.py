import unittest
from atendimentos_mock import AtendimentosMock

class TestAtendimentos(unittest.TestCase):

    def setUp(self):
        self.atendimentos_mock = AtendimentosMock().get_mock()
        self.atendimentos = self.atendimentos_mock.get_atendimentos()

    #Testes de sucesso

    #Testes falha

if __name__ == '__main__':
    unittest.main()
