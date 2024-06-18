import unittest
from refactor_app import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.cg = CalculaGanador()

    def test_es_dni_valido(self):
        self.assertTrue(self.cg.es_dni_valido("12345678"))
        self.assertFalse(self.cg.es_dni_valido("1234567"))
        self.assertFalse(self.cg.es_dni_valido("123456789"))
        self.assertFalse(self.cg.es_dni_valido("abcdefgh"))

    def test_calcularganador(self):

        datatest = self.cg.leerdatos()
        self.assertEqual(self.cg.calcularganador(datatest), ['Dennis Reyna', 'Aundrea Grace'])

        datatest_2 = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.assertEqual(self.cg.calcularganador(datatest_2), ['Aundrea Grace'])

        datatest_3 = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.assertEqual(self.cg.calcularganador(datatest_3), ['Eddie Hinesley'])

if __name__ == "__main__":
    unittest.main()
