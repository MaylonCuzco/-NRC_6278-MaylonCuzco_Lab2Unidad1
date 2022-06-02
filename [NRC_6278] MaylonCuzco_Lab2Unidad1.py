#importamos la libreria queue
from queue import Queue

class Grafo:
    def __init__(self, num_nodos, dirigido=True):
        ''' Se crea la clase del grafo 
        PARÁMETROS:
            num_nodos: De tipo entero, nos muestra el numero de nodos
            dirigido: De tipo booleano, se especifica si el grafo es dirigido o no dirigido
        ATRIBUTOS:
            m_num_nodos: De tipo entero, muestra el numero de nodos
            m_dirijido: De tipo booleano, indica si el grafo es o no dirigido.
            m_nodos: Rango de los nodos
            m_lista_ady: Diccionario, implementa la lista de adyacencia
        '''
        self.m_num_nodos = num_nodos 
        #La función range nos perimte retorna la sucesion del numero de nodos
        self.m_nodos = range(self.m_num_nodos) 

        # DIRIGIDO O NO DIRIGIDO
        #Especificamos que el atributo "m_dirigido" es tipo booleano 
        self.m_dirigido = dirigido 
		
        # Representación gráfica - Lista de adyacencia
        # Usamos un diccionario para implementar una lista de adyacencia
        #Se especifica que el atributo "m_lista_ady" tendra un conjunto vasio "set()" 
        # mediante un bucle for el nodo contara con el atributo "m_nodos"
        self.m_lista_ady = {nodo: set() for nodo in self.m_nodos}      
    