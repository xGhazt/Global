from typing import List
from random import choice

class Detector:
    def __init__(self, nombre: str, sensibilidad: float):

        self.nombre = nombre
        self.sensibilidad = sensibilidad

    def detectar_mutantes(self, matriz: List[str]) -> bool:
        return any([
            self.detectar_horizontal(matriz),
            self.detectar_vertical(matriz),
            self.detectar_diagonal(matriz)
        ])

    def detectar_horizontal(self, matriz: List[str]) -> bool:
        for fila in matriz:
            if any(fila[i:i+4] == fila[i] * 4 for i in range(len(fila) - 3)):
                return True
        return False
    """esto de acá busca si hay 4 letras seguidas iguales, divide las filas en pedacitos de 4 y se fija si alguno se repite las 4 veces, si lo hace devuelve un -hay un mutante-"""

    def detectar_vertical(self, matriz: List[str]) -> bool:
        for col in range(len(matriz[0])):
            columna = ''.join([fila[col] for fila in matriz])
            if any(columna[i:i+4] == columna[i] * 4 for i in range(len(columna) - 3)):
                return True
        return False
    """esto de acá hace lo mismo que el anterior pero buscando en pedacitos de columnas"""

    def detectar_diagonal(self, matriz: List[str]) -> bool:
        size = len(matriz)
        for i in range(size - 3):
            for j in range(size - 3):
                if (matriz[i][j] == matriz[i+1][j+1] == matriz[i+2][j+2] == matriz[i+3][j+3]):
                    return True
                if (matriz[i][j+3] == matriz[i+1][j+2] == matriz[i+2][j+1] == matriz[i+3][j]):
                    return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada: str, potencia: int):
        self.base_nitrogenada = base_nitrogenada
        self.potencia = potencia

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def crear_mutante(self, matriz: List[str], posicion_inicial: int, orientacion: str) -> List[str]:
        try:
            if orientacion == "H":
                matriz[posicion_inicial] = (
                    matriz[posicion_inicial][:2]
                    + self.base_nitrogenada * 4
                    + matriz[posicion_inicial][6:]
                )
            elif orientacion == "V":
                for i in range(4):
                    fila = list(matriz[posicion_inicial + i])
                    fila[2] = self.base_nitrogenada
                    matriz[posicion_inicial + i] = ''.join(fila)
            return matriz
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz

class Virus(Mutador):
    def crear_mutante(self, matriz: List[str], posicion_inicial: int) -> List[str]:
        try:
            for i in range(4):
                fila = list(matriz[posicion_inicial + i])
                fila[posicion_inicial + i] = self.base_nitrogenada
                matriz[posicion_inicial + i] = ''.join(fila)
            return matriz
        except Exception as e:
            print(f"Error al crear mutante diagonal: {e}")
            return matriz
        
class Sanador:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def sanar_mutantes(self, matriz: List[str]) -> List[str]:
        detector = Detector("Sanador Detector", 0.9)
        if detector.detectar_mutantes(matriz):
            print("Se detectaron mutantes. Generando nueva matriz desmutada, por favor, espere.")
            return self._generar_adn()
        return matriz

    def _generar_adn(self) -> List[str]:
        bases = ["A", "T", "C", "G"]
        nueva_matriz = [
            ''.join(choice(bases) for _ in range(6)) for _ in range(6)
        ]
        detector = Detector("Sanador Detector", 0.9)
        while detector.detectar_mutantes(nueva_matriz):
            nueva_matriz = [
                ''.join(choice(bases) for _ in range(6)) for _ in range(6)
            ]
        return nueva_matriz