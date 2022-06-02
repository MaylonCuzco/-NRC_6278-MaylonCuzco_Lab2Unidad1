from queue import Queue
'''importamos la libreria queue'''
class Grafo:
    def __init__(self, num_nodos, dirigido=True):
        ''' Constructor
        PARÁMETROS:
            num_nodos: 
                De tipo entero, nos muestra el numero de nodos
            dirigido: 
                De tipo booleano, se especifica si el grafo es dirigido o no dirigido
        ATRIBUTOS:
            m_num_nodos: 
                De tipo entero, muestra el numero de nodos
            m_dirijido: 
                De tipo booleano, indica si el grafo es o no dirigido.
            m_nodos: 
                Rango de los nodos
            m_lista_ady: 
                Diccionario, implementa la lista de adyacencia
        '''
        self.m_num_nodos = num_nodos 
        ''' La función range nos perimte retorna la sucesion del numero de nodos '''
        self.m_nodos = range(self.m_num_nodos) 
        '''
         DIRIGIDO O NO DIRIGIDO
        '''
        self.m_dirigido = dirigido 
		
        '''
         Representación gráfica - Lista de adyacencia
         Usamos un diccionario para implementar una lista de adyacencia
         Se especifica que el atributo "m_lista_ady" tendra un conjunto vasio "set()" 
         mediante un bucle for el nodo contara con el atributo "m_nodos"
        '''
        self.m_lista_ady = {nodo: set() for nodo in self.m_nodos}      
    

    def agregar_borde(self, nodo1, nodo2, peso=1):
        ''' Se agrega los bordes 
         PARÁMETROS:
            nodo1: 
                De tipo entero, el nodo que genera los bordes
            nodo2: 
                De tipo entero, el nodo que es parte del borde
            peso: 
                De valor 1 establecido
         ATRIBUTOS
            m_lista_ady: 
                Diccionario de la lista adyacente
            m_dirigido: 
                Booleano, indica si es o no dirigido
         
         Definimos la función  agregar_borde la cual contrendra los parámetros de los nodos 1 y 2,
         al igual que el peso de los nodos.
         Especificamos el parámetro m_lista_ady el cual tendra como primer valor
         el nodo 1 y se añade al node 2 y el peso de este.
        '''
        self.m_lista_ady[nodo1].add((nodo2, peso))
        '''
         En caso contrario de ser falso el parametro establecido anteriormente m_dirigido,
         se tiene como prier valor el nodo 2 y se añade el nodo 1 y el peso
        '''
        if not self.m_dirigido:
            self.m_lista_ady[nodo2].add((nodo1, peso))
    

    def imprime_lista_ady(self):
        '''Se imprime la representacion del grafo
        PARÁMETROS:
            Sin parámetros
        ATRIBUTOS:
            m_lista_ady: 
                Diccionario del grafo


        Se inicializa un bucle for en el cual se establece una variable key 
        el cual hace refencia a las llaves "{}" dentro de la lista de los nodos
        '''
        for key in self.m_lista_ady.keys():
            ''' Se estable que en al iprimir la lista de nodos se tendra
                que colocar primero la expresion "nodos" seguido
                de una llave abierta establecida por la variable "key" 
                seguido de la expresion ":" y imprime la lista de 
                nodos especificando que termina con cerrando las llaves
            '''
            print("Nodo", key, ": ", self.m_lista_ady[key])


    def bfs_transversal(self, inicio_nodo):
        ''' Muestra el recorrido BFS (algoritmo de busqueda que recorre los nodos del grafo)
        PARÁMETRO:
            inicio_nodo: 
                De tipo entero, nodo por el que comienza el recorrido
        ATRIBUTO:
            m_lista_ady: 
                Diccionario de la lista adyacente
        
        Declaramos una variable de nombre "visitado" el cual almacenará
        un conjunto de elementos medinate el "set()" 
        '''
        visitado = set()
        ''' Definimos la variable querue el cual mediante la libreria
        que se importo de Queue() nos permite implementar
        una cola de datos en este caso hace refencia a los nodos 
        '''
        queue = Queue()
        '''
        Agregue inicio_nodo a la cola y la lista visitada
        Especificamos que la variable "queue" mediante la instancia "put" 
        realiza una peticion al parametro "inicio_nodo"
        '''
        queue.put(inicio_nodo)
        ''' En la variable "visitado" se almacena el parámetro "inicio_nodo" '''
        visitado.add(inicio_nodo)

        ''' 
        Mediante la funcion while le decimos que en caso que la variable queue 
        no realice la peticion  
        '''
        while not queue.empty():
            ''' 
            Descola un vértice de la cola e imprimirlo
            mediante la variable "nodo_actual" nos devolera el valor del nodo  
            '''
            nodo_actual = queue.get()
            ''' imprimimos el recorrido de los nodos  '''
            print(nodo_actual, end = " ")
            '''
            Obtenga todos los vértices adyacentes del vértice eliminado.
            Si un adyacente no ha sido visitado, márquelo como visitado y póngalo en cola
            
            Especificamos los parametros que se van a ocupara en la impresion de la lista,
            en donde se recorre cada nodo
            '''
            for (siguiente_nodo, peso) in self.m_lista_ady[nodo_actual]:
                if siguiente_nodo not in visitado:
                    queue.put(siguiente_nodo)
                    visitado.add(siguiente_nodo)
    

if __name__ == "__main__":
    '''#### Ejemplo #####'''

    ''' 
    Crear una instancia de la clase `Grafico`
    Este gráfico no está dirigido y tiene 5 nodos
    '''
    g = Grafo(5, dirigido= False)

    ''' Agregue bordes al gráfico con peso predeterminado = 1 '''
    g.agregar_borde(0, 1)
    g.agregar_borde(0, 2)
    g.agregar_borde(1, 2)
    g.agregar_borde(1, 4)
    g.agregar_borde(2, 3)

    ''' Imprime la lista de adyacencia en el formulario nodo n: {(nodo, peso)} '''
    g.imprime_lista_ady( )

    print ("Lo que sigue es el recorrido primero en anchura (a partir del vértice 0)")
    g.bfs_transversal(0)
    print( ) 