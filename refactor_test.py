import unittest
from refactor_app import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.cg = CalculaGanador()


    def test_leerdatos_csv(self):
        self.assertEqual(self.cg.leerdatos_csv('2024.csv'), [
            [
                'Ancash', 'Asuncion', 'Chacas', '81122156', 'Eddie Hinesley', '1'
            ]
        ])

        self.assertEqual(self.cg.leerdatos_csv('test.csv'), [
            [
                'Ancash', 'Asuncion', 'Chacas', '20398144', 'Paula Daigle', '1'
            ],
            [
                'Ancash','Asuncion','Chacas','33656332','Aundrea Grace','0'
            ]
        ])

        with self.assertRaises(FileNotFoundError, msg=('El archivo 0204_noexiste.csv no existe.')):
            self.cg.leerdatos_csv('0204_noexiste.csv')

    def test_es_dni_valido(self):
        self.assertTrue(self.cg.es_dni_valido("12345678"))
        self.assertFalse(self.cg.es_dni_valido("1234567"))
        self.assertFalse(self.cg.es_dni_valido("123456789"))
        self.assertFalse(self.cg.es_dni_valido("abcdefgh"))

    def test_calcularganador(self):

        datatest = self.cg.leerdatos_csv()
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
