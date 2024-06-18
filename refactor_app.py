import csv
import re
from collections import defaultdict

class CalculaGanador:

    def leerdatos(self, filename='0204.csv'):
        """
        Lee los datos del archivo CSV y devuelve una lista de filas de datos.
        """
        data = []
        with open(filename, 'r') as csvfile:
            next(csvfile)  
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def es_dni_valido(self, dni):
        """
        Verifica si un DNI es válido (debe tener exactamente 8 dígitos).
        """
        return bool(re.match(r'^\d{8}$', dni))

    def calcularganador(self, data):
        """
        Calcula el ganador de los votos válidos.
        """
        votosxcandidato = defaultdict(int)
        total_votos_validos = 0

        for fila in data:
            dni, candidato, esvalido = fila[3], fila[4], fila[5]
            if self.es_dni_valido(dni) and esvalido == '1':
                votosxcandidato[candidato] += 1
                total_votos_validos += 1

        if not votosxcandidato:
            return []

        # Ordenar los candidatos por número de votos válidos en orden descendente
        ordenado = sorted(votosxcandidato.items(), key=lambda item: item[1], reverse=True)
        
        # Verificar si hay un ganador con más del 50% de los votos válidos
        for candidato, votos in ordenado:
            #print(candidato, votos)
            if votos > total_votos_validos / 2:
                return [candidato]
            
        # Si no hay un ganador, retornar los dos candidatos con más votos válidos
        return [candidato for candidato, votos in ordenado[:2]]

        

