import unittest
from atendimentos_mock import AtendimentosMock

class TestAtendimentos(unittest.TestCase):

    def setUp(self):
        self.atendimentos_mock = AtendimentosMock().get_mock()
        self.atendimentos = self.atendimentos_mock.get_atendimentos()

    #---------------------------------Testes Sucesso-------------------------------------------#
    def test_horario_professor_rafael(self):
        professor = next((p for p in self.atendimentos if p["id"] == 6), None)
        self.assertIsNotNone(professor, "Professor com ID 6 não encontrado")
        self.assertEqual(professor["horario"], "17:30", "Horario do professor com ID 6 deve ser '17:30'")

    def test_predio_professor_yvo(self):
        professor = next((p for p in self.atendimentos if p["id"] == 7), None)
        self.assertIsNotNone(professor, "Professor com ID 7 não encontrado")
        self.assertEqual(professor["predio"], 4, "Predio do professor com ID 7 deve ser 4")

    #---------------------------------Testes Falhas-------------------------------------------#

    def test_periodo_professor_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 2), None)
        self.assertIsNotNone(professor, "Professor com ID 2 não encontrado")
        self.assertNotEqual(professor["periodo"], "Noturno", "Periodo do professor com ID 2 não deve ser 'Noturno'")

    def test_sala_professor_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 3), None)
        self.assertIsNotNone(professor, "Professor com ID 3 não encontrado")
        self.assertNotEqual(professor["sala"], 2, "Sala do professor com ID 3 não deve ser 17")

    

if __name__ == '__main__':
    unittest.main()
