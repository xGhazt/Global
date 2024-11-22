from typing import List
from random import choice

from Clases import Detector, Radiacion, Virus, Sanador

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

def main():
    print("\n---Bienvenido al simulador de ADN---")
    print("1. Crear matriz personalizada")
    print("2. Usar matriz predefinida")
    print("")
    opcion = input("Seleccione una opción (1/2): ").strip()

    if opcion == "1":
        matriz = crear_matriz()
    elif opcion == "2":
        matriz = [
            "AATACA", "GATTCA", "CAACAT",
            "GGGCTA", "ATTGCG", "CTGTTC"
        ]
    else:
        print("")
        print("### Opción inválida. Finalizando programa. ###")
        return
    
    

    while True:
        print("\nMatriz actual:")
        print("----------ADN----------")
        contador=0
        print("  0   1   2   3   4   5")
        for fila in matriz:
            print(contador, " | ".join(fila))  
            contador+=1 
        print("-----------------------")

        print("\n¿Qué desea hacer?")
        print("1. Detectar mutantes")
        print("2. Crear mutación")
        print("3. Sanar mutantes")
        print("4. Salir")
        opcion = input("Ingrese una opción (1/2/3/4): ").strip()

        if opcion == "1":
            detector = Detector(matriz)
            detector.detectar_mutantes()
            if detector.mutacion == False:
                print("\nNo hay mutaciones")
            else:
                print("\nHay una mutación")
            
        elif opcion == "2":
            print("\nOpciones de mutación:")
            print("1. Usar Radiación (horizontal o vertical)")
            print("2. Usar Virus (diagonal)\n")
            mutacion = input("Seleccione un tipo de mutación (1/2): ").strip()
            if mutacion not in ["1","2"]:
                    print("\n###() Opción inválida. Intente de nuevo. ()###")
                    continue
            print("")
            base = input("Ingrese la base nitrogenada para la mutación (A/T/C/G): ").strip().upper()
            print("")
            if base not in ["A", "T", "C", "G"]:
                    print("###() Base nitrogenada inválida. Intente de nuevo. ()###")
                    continue


            if mutacion == "1":

                orientacion = input("Ingrese orientación (H para horizontal, V para vertical): ").strip().upper()
                if orientacion not in ["H", "V"]:
                    print("###() Orientación inválida. Intente de nuevo. ()###")
                    continue
                try:
                    posicion_inicial = input("\nIngrese una posicion x,y (fila, columna -- sin parentesis -- ejemplo: 0,3): ")
                    print("")
                    
                    posicion_inicial = map(int, posicion_inicial.split(","))
                    
                    radiacion = Radiacion(base,matriz)
                    
                    matriz = radiacion.crear_mutante(base, posicion_inicial, orientacion)

                    if radiacion.estado_mutacion == "Exitosa":
                        print("Mutación aplicada con éxito!!!")
                    
                except ValueError:
                    print("###() Posición inválida. no olvide la coma, ejemplo: 3,2 ()###" )
                    
            elif mutacion == "2":

                try:
                    posicion_inicial = input("\nIngrese una posicion x,y (fila, columna -- sin parentesis -- ejemplo: 0,3): ")
                    print("")

                    posicion_inicial = map(int, posicion_inicial.split(","))
                    
                    virus = Virus(base, matriz)

                    matriz = virus.crear_mutante(base, posicion_inicial)

                    if virus.estado_mutacion == "Exitosa":
                        print("Mutación aplicada con éxito!!!")

                except ValueError:
                    print("###() Posición inválida. no olvide la coma, ejemplo: 3,2 ()###" )
            else:
                print("###() Tipo de mutación inválido. Intente de nuevo. ()###")

        elif opcion == "3":
            sanador=Sanador(matriz)
            matriz=sanador.sanar_mutantes()
            
        elif opcion == "4":
            print("¡Gracias por usar el simulador de ADN! Hasta pronto.")
            break
        else:
            print("###() Opción inválida. Intente de nuevo. ()###")

if __name__ == "__main__":
    main()
