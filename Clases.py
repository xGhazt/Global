from typing import List
from random import choice

'''**************************************************************************************************************************'''
        

class Detector:
    def __init__(self, adn):
        self.adn=adn
        self.mutacion=False

    def detectar_mutantes(self):
        
        if (self.detectar_mutacion_horizontal() or
            self.detectar_mutacion_vertical() or
            self.detectar_mutacion_diagonal()):

            return self.mutacion
        else:            
            
            return self.mutacion


        
    '''DETECTAR MUTACION HORIZONTAL'''

    def detectar_mutacion_horizontal(self):

        '''
            se analiza fila por fila, buscando una secuencia repetida 4 veces de una misma base
        '''
        for fila in self.adn:
            
            contador=0
            for j in range (5):
                if fila[j] == fila[j+1]:
                    contador += 1
                else:
                    contador=0

                if contador == 3:
                    
                    self.mutacion=True

                    return self.mutacion
           
        return False       
        
    '''DETECTAR MUTACION VERTICAL'''
    def detectar_mutacion_vertical(self):

        '''
            similar al enfoque anterior, solo que esta vez es columna por columna
        '''

        for columna in range(6):
            
            contador = 0
            base_anterior = None  

            for fila in self.adn:  
                base = fila[columna] 
                if base == base_anterior:  
                    contador += 1
                else:
                    contador = 0  

                base_anterior = base 
                
                if contador == 3: 
                    
                    self.mutacion=True

                    return self.mutacion
                
        return False


    '''DETECTAR MUTACION DIAGONAL'''

    def detectar_mutacion_diagonal(self):

        '''buscar en diagonales principales(descendentes) de izquierda a derecha'''
        for fila in range(3):  
            for columna in range(3):  
                if (self.adn[fila][columna] == self.adn[fila + 1][columna + 1] ==
                    self.adn[fila + 2][columna + 2] == self.adn[fila + 3][columna + 3]):
                    
                    self.mutacion=True

                    return self.mutacion

        '''buscar en diagonales secundarias(ascendentes) de derecha a izquierda'''
        
        for fila in range(3, 6):  
            for columna in range(3):  
                if (self.adn[fila][columna] == self.adn[fila - 1][columna + 1] ==
                    self.adn[fila - 2][columna + 2] == self.adn[fila - 3][columna + 3]):
                    
                    self.mutacion=True

                    return self.mutacion

        return self.mutacion


'''**************************************************************************************************************************'''

class Mutador:

    estado_mutacion="pendiente"

    def __init__(self, base_nitrogenada, matriz_adn):
        self.base_nitrogenada = base_nitrogenada
        self.matriz_adn = [list(fila) for fila in matriz_adn]

        '''cambiamos la matriz de cadenas, por una matriz de caracteres individuales por fila,
           para poder trabajar mejor sobre las posiciones'''
        

    def crear_mutante(self):
        pass
    
'''**************************************************************************************************************************'''

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada, matriz_adn)

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion):

        fila, columna = (posicion_inicial)
        
        try:
            

            if ( fila < 0 or columna < 0 ) or ( fila  >= len(self.matriz_adn) ) or ( columna  >= len(self.matriz_adn[0]) ):
               self.estado_mutacion = "Fallida :( "
               raise IndexError("La posición se sale de los límites de la matriz.")
        

            '''
                dependiendo la posicion incial es con lo que se trabaja, porque hay un limite, donde
                al querer mutar se pasaria del limite de la matriz, por eso si la columna es mayor o igual a 3
                lo que se hace es simular un llenado de derecha a izquierda, simulando que la posicion inicial
                estara a la derecha
            '''
            
            if orientacion == "H":
                if columna + 3 >= len(self.matriz_adn[0]):
                    
                    for i in range(4):
                        self.matriz_adn[fila][(columna-3) + i] = base_nitrogenada
                    
                else:    
                    
                    for i in range(4):
                        self.matriz_adn[fila][columna + i] = base_nitrogenada
                    

                '''
                    de igual manera con las horizontales, solamente que se tomara en cuenta la fila y no la columna
                    haciendo el mismo proceso, al llegar el limite se llenara de "abajo hacia arriba", y si no pasa
                    el limite de arriba hacia abajo
                '''

            elif orientacion == "V":
                if fila + 3 >= len(self.matriz_adn):
                    for i in range(4):
                        self.matriz_adn[(fila-3) + i][columna] = base_nitrogenada
                    
                else:            
                    for i in range(4):
                        self.matriz_adn[fila + i][columna] = base_nitrogenada

            self.estado_mutacion = "Exitosa"
        
        except IndexError as e:
            print(f"*****************\nESTADO DE LA MUTACIÓN: {self.estado_mutacion} \n*****************")
            print(f"Error de índice: {e} \n*****************")


        '''
        transformamos la matriz de caracteres individuales, a la matriz de cadenas original, la cual cambiamos en la superclase
        '''
        
        self.matriz_adn = [''.join(fila) for fila in self.matriz_adn]
        
        return self.matriz_adn
    
'''**************************************************************************************************************************'''

class Virus(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada, matriz_adn)
        

    def crear_mutante(self, base_nitrogenada, posicion_inicial):

        fila, columna = (posicion_inicial)

        try:
            
            if ( fila < 0 or columna < 0 ) or ( fila  >= len(self.matriz_adn) ) or ( columna  >= len(self.matriz_adn[0]) ):
               self.estado_mutacion = "Fallida :( "
               raise IndexError("La posición se sale de los límites de la matriz.")
        
            
            '''
                analizamos cada caso donde la posicion inicial puede ser invalida en una direccion pero en otra no,
                la posicion inicial la puede tomar tanto de izquierda a derecha como de derecha a izquierda, ya que siempre
                habran dos extremos osea dos posibles posiciones iniciales
            '''
            
            if (fila >= 3 and columna <= 2):

                for i in range(4):
                    self.matriz_adn[fila - i][columna + i] = base_nitrogenada                

            elif (fila <= 2 and columna >= 3):

                for i in range(4):
                    self.matriz_adn[fila + i][columna - i] = base_nitrogenada  

            elif (fila >= 3 and columna >= 3):

                for i in range(4):
                    self.matriz_adn[(fila-3) + i][(columna-3) + i] = base_nitrogenada

            else:

                for i in range(4):
                    self.matriz_adn[fila + i][columna + i] = base_nitrogenada
        
            self.estado_mutacion = "Exitosa"
        except IndexError as e:
            print(f"*****************\nESTADO DE LA MUTACIÓN: {self.estado_mutacion} \n*****************")
            print(f"Error de índice: {e} \n*****************")

        
        '''
        transformamos la matriz de caracteres individuales, a la matriz de cadenas original, la cual cambiamos en la superclase
        '''

        self.matriz_adn = [''.join(fila) for fila in self.matriz_adn]

        
        return self.matriz_adn


'''**************************************************************************************************************************'''

class Sanador:

    
    def __init__(self, matriz):
        self.matriz = matriz
        self.sanacion_aplicada = False
        

    def sanar_mutantes(self) :
        
        detector=Detector(self.matriz)
        
        if detector.detectar_mutantes():
            print("Se detectaron mutantes. Generando nueva matriz desmutada, por favor, espere.")
            return self._generar_adn()
        else:
            
            if self.sanacion_aplicada == False:
                print("\nEl ADN ya está sano, no tiene mutaciones")

                return self.matriz
            else:
                print("\nEste ADN ya ha sido sanado previamente")        
                return self.matriz
        


    def _generar_adn(self) -> List[str]:
        bases = ["A", "T", "C", "G"]
        nueva_matriz = [
            ''.join(choice(bases) for _ in range(6)) for _ in range(6)
        ]
        
        detector=Detector(nueva_matriz)
        self.matriz = nueva_matriz
        

        while detector.detectar_mutantes():
    
            nueva_matriz = [
                ''.join(choice(bases) for _ in range(6)) for _ in range(6)
            ]
            detector=Detector(nueva_matriz)
            self.matriz = nueva_matriz

        self.sanacion_aplicada = True
        print("---- ADN sanado ----")
        return self.matriz
    

