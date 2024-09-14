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

    def test_nome_professor_renzo(self):
        professor = next((p for p in self.atendimentos if p["id"] == 1), None)
        self.assertIsNotNone(professor, "Professor com ID 1 não encontrado")
        self.assertEqual(professor["professor"], "Renzo", "Nome do professor com ID 1 deve ser 'Renzo'")

    def test_predio_professor_alessandra(self):
        professor = next((p for p in self.atendimentos if p["id"] == 5), None)
        self.assertIsNotNone(professor, "Professor com ID 5 não encontrado")
        self.assertEqual(professor["predio"], 4, "Predio do professor com ID 5 deve ser 4")

    def test_nome_professor_karina(self):
        professor = next((p for p in self.atendimentos if p["id"] == 4), None)
        self.assertIsNotNone(professor, "Professor com ID 4 não encontrado")
        self.assertEqual(professor["professor"], "Karina", "Nome do professor com ID 4 deve ser 'Karina'")

    def test_predio_professor_rafael(self):
        professor = next((p for p in self.atendimentos if p["id"] == 6), None)
        self.assertIsNotNone(professor, "Professor com ID 6 não encontrado")
        self.assertEqual(professor["predio"], 6, "Prédio do professor com ID 6 deve ser 6")



    #---------------------------------Testes Falhas-------------------------------------------#

    def test_periodo_professor_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 2), None)
        self.assertIsNotNone(professor, "Professor com ID 2 não encontrado")
        self.assertNotEqual(professor["periodo"], "Noturno", "Periodo do professor com ID 2 não deve ser 'Noturno'")

    def test_sala_professor_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 3), None)
        self.assertIsNotNone(professor, "Professor com ID 3 não encontrado")
        self.assertNotEqual(professor["sala"], 2, "Sala do professor com ID 3 não deve ser 17")

    def test_professor_inexistente(self):
        professor = next((p for p in self.atendimentos if p["id"] == 99), None)
        self.assertIsNone(professor, "Professor com ID 99 não deveria existir")


    def test_nome_professor_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 1), None)
        self.assertIsNotNone(professor, "Professor com ID 1 não encontrado")
        self.assertNotEqual(professor["professor"], "Alves, o capitao monitor", "Nome do professor com ID 1 não deve ser 'Alves, o capitao monitor'")

    def test_predio_professor_chris(self):
        professor = next((p for p in self.atendimentos if p["id"] == 3), None)
        self.assertIsNotNone(professor, "Professor com ID 3 não encontrado")
        self.assertEqual(professor["predio"], 4, "Prédio do professor com ID 3 deve ser 4")

    def test_nome_professor_soned_incorreto(self):
        professor = next((p for p in self.atendimentos if p["id"] == 2), None)
        self.assertIsNotNone(professor, "Professor com ID 2 não encontrado")
        self.assertNotEqual(professor["professor"], "Maria", "Nome do professor com ID 2 não deve ser 'Maria'")



    

if __name__ == '__main__':
    unittest.main()
