from typing import List
from random import choice

from Clases import Detector, Mutador, Radiacion, Virus, Sanador

def crear_matriz() -> List[str]:
    print("Ingrese su matriz de ADN fila por fila. Deben ser 6 filas de exactamente 6 caracteres con bases nitrogenadas válidas (A, T, C, G).")
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"Ingrese la fila {i + 1} (6 letras): ").strip().upper()
            if len(fila) == 6 and all(base in "ATCG" for base in fila):
                matriz.append(fila)
                break
            else:
                print("Error: La fila debe tener exactamente 6 letras y solo puede contener A, T, C o G.")
    return matriz
"""Resumiendo, el menú lo que hace es que te deja elegir entre crear una matriz o usar una predefinida, si querés hacerla manual te va a pedir q
la ingreses fila por fila, se ingresa todo junto, por ejemplo, en la primer fila se ingresa AATTGG y así con las otras PD: me sale como que el 
mutador a la hora de importarlo no hace nada pero dentro de lo que es el codigo funciona igual, esta raro"""
def main():
    print("---Bienvenido al simulador de ADN---")
    print("1. Crear matriz personalizada")
    print("2. Usar matriz predefinida")
    opcion = input("Seleccione una opción (1/2): ").strip()

    if opcion == "1":
        matriz = crear_matriz()
    elif opcion == "2":
        matriz = [
            "AGATCA", "GATTCA", "CAACAT",
            "GAGCTA", "ATTGCG", "CTGTTC"
        ]
    else:
        print("Opción inválida. Finalizando programa.")
        return

    while True:
        print("\nMatriz actual:")
        for fila in matriz:
            print(fila)

        print("\n¿Qué desea hacer?")
        print("1. Detectar mutantes")
        print("2. Crear mutación")
        print("3. Sanar mutantes")
        print("4. Salir")
        opcion = input("Ingrese una opción (1/2/3/4): ").strip()

        if opcion == "1":
            detector = Detector("Detector General", 0.8)
            es_mutante = detector.detectar_mutantes(matriz)
            print("Se detectó un mutante." if es_mutante else "No se detectaron mutantes.")
        elif opcion == "2":
            print("\nOpciones de mutación:")
            print("1. Usar Radiación (horizontal o vertical)")
            print("2. Usar Virus (diagonal)")
            mutacion = input("Seleccione un tipo de mutación (1/2): ").strip()

            if mutacion == "1":
                orientacion = input("Ingrese orientación (H para horizontal, V para vertical): ").strip().upper()
                if orientacion not in ["H", "V"]:
                    print("Orientación inválida. Intente de nuevo.")
                    continue
                try:
                    posicion = int(input("Ingrese la posición inicial (0-5): "))
                    if not 0 <= posicion <= 5:
                        raise ValueError
                    radiacion = Radiacion("T", 5)
                    matriz = radiacion.crear_mutante(matriz, posicion, orientacion)
                    print("Mutación aplicada con éxito.")
                except ValueError:
                    print("Posición inválida. Debe ser un número entre 0 y 5.")
            elif mutacion == "2":
                try:
                    posicion = int(input("Ingrese la posición inicial (0-2 para permitir espacio diagonal): "))
                    if not 0 <= posicion <= 2:
                        raise ValueError
                    virus = Virus("T", 5)
                    matriz = virus.crear_mutante(matriz, posicion)
                    print("Mutación aplicada con éxito.")
                except ValueError:
                    print("Posición inválida. Debe ser un número entre 0 y 2.")
            else:
                print("Tipo de mutación inválido. Intente de nuevo.")
        elif opcion == "3":
            sanador = Sanador("Sanador Maestro")
            matriz = sanador.sanar_mutantes(matriz)
            print("Se ha sanado la matriz.")
        elif opcion == "4":
            print("¡Gracias por usar el simulador de ADN! Hasta pronto.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
