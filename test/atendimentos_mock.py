from unittest.mock import Mock

class AtendimentosMock:
    def __init__(self):
        self.mock = Mock()
        self.setup_mock()
    
    def setup_mock(self):
        self.mock.get_atendimentos.return_value = [
            {
                "id": 1,
                "professor": "Renzo",
                "horario": "17:30",
                "periodo": "Integral",
                "sala": 12,
                "predio": 3
            },
            {
                "id": 2,
                "professor": "Soned",
                "horario": "10:00",
                "periodo": "Integral",
                "sala": 2,
                "predio": 1
            },
            {
                "id": 3,
                "professor": "Chris",
                "horario": "19:10",
                "periodo": "Noturno",
                "sala": 17,
                "predio": 4
            },
            {
                "id": 4,
                "professor": "Karina",
                "horario": "21:00",
                "periodo": "Noturno",
                "sala": 22,
                "predio": 6
            },
            {
                "id": 5,
                "professor": "Alessandra",
                "horario": "15:30",
                "periodo": "Integral",
                "sala": 20,
                "predio": 4
            },
            {
                "id": 6,
                "professor": "Rafael",
                "horario": "17:30",
                "periodo": "Integral",
                "sala": 21,
                "predio": 6
            },
            {
                "id": 7,
                "professor": "Yvo",
                "horario": "10:00",
                "periodo": "Integral",
                "sala": 16,
                "predio": 4
            },
            {
                "id": 8,
                "professor": "Francisco",
                "horario": "21:30",
                "periodo": "Noturno",
                "sala": 8,
                "predio": 2
            }
        ]

    def get_mock(self):
        return self.mock
