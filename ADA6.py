class GrafoEstados:
    def __init__(self):
        # Inicializar el grafo y la lista de estados
        self.grafo = {}
        self.estados = []
        
    def agregar_estado(self, estado):
        if estado not in self.estados:
            self.estados.append(estado)
            # Inicializar el diccionario para las conexiones del estado
            if estado not in self.grafo:
                self.grafo[estado] = {}
            
    def agregar_conexion(self, estado1, estado2, costo):
        # Asegurarse de que ambos estados existan en el grafo
        self.agregar_estado(estado1)
        self.agregar_estado(estado2)
        # Agregar la conexión en ambas direcciones
        self.grafo[estado1][estado2] = costo
        self.grafo[estado2][estado1] = costo
        
    def recorrido_sin_repeticion(self, estado_inicial):
        visitados = []
        costo_total = 0
        estado_actual = estado_inicial
        
        while len(visitados) < len(self.estados):
            visitados.append(estado_actual)
            siguiente = None
            min_costo = float('inf')
            
            # Buscar el siguiente estado no visitado con menor costo
            for estado_vecino, costo in self.grafo[estado_actual].items():
                if estado_vecino not in visitados and costo < min_costo:
                    siguiente = estado_vecino
                    min_costo = costo
                    
            if siguiente:
                costo_total += min_costo
                estado_actual = siguiente
            else:
                break
                
        return visitados, costo_total
    
    def recorrido_con_repeticion(self, estado_inicial):
        visitados = []
        costo_total = 0
        estado_actual = estado_inicial
        estados_count = {}
        
        # Inicializar el contador de estados
        for estado in self.estados:
            estados_count[estado] = 0
        
        # Continuar hasta visitar todos los estados al menos una vez
        while len(set(visitados)) < len(self.estados) or max(estados_count.values()) < 3:
            visitados.append(estado_actual)
            estados_count[estado_actual] += 1
            
            # Elegir el siguiente estado
            siguiente = None
            min_costo = float('inf')
            
            for estado_vecino, costo in self.grafo[estado_actual].items():
                if estados_count[estado_vecino] < 3 and costo < min_costo:
                    siguiente = estado_vecino
                    min_costo = costo
            
            if siguiente:
                costo_total += min_costo
                estado_actual = siguiente
            else:
                break
                
        return visitados, costo_total
    
    def mostrar_relaciones(self):
        print("\nRelaciones entre estados:")
        print("=" * 50)
        for estado1 in sorted(self.grafo.keys()):
            print(f"\n{estado1} se conecta con:")
            for estado2, costo in sorted(self.grafo[estado1].items()):
                print(f"  └─ {estado2} (costo: ${costo})")

    def mostrar_grafo_ascii(self):
        print("\nRepresentación ASCII del grafo:")
        print("=" * 50)
        print("Formato: Estado -> (Costo) -> Estado")
        print("-" * 50)
        conexiones_mostradas = set()
        
        for estado1 in sorted(self.grafo.keys()):
            for estado2, costo in sorted(self.grafo[estado1].items()):
                # Evitar mostrar conexiones duplicadas
                if (estado1, estado2) not in conexiones_mostradas and \
                   (estado2, estado1) not in conexiones_mostradas:
                    print(f"{estado1} --(${costo})--> {estado2}")
                    conexiones_mostradas.add((estado1, estado2))

# Crear instancia del grafo
grafo = GrafoEstados()

# Agregar estados y sus conexiones
grafo.agregar_conexion("Jalisco", "Michoacán", 300)
grafo.agregar_conexion("Jalisco", "Guanajuato", 250)
grafo.agregar_conexion("Michoacán", "Estado de México", 200)
grafo.agregar_conexion("Guanajuato", "Estado de México", 350)
grafo.agregar_conexion("Estado de México", "CDMX", 50)
grafo.agregar_conexion("CDMX", "Morelos", 100)
grafo.agregar_conexion("Morelos", "Guerrero", 200)
grafo.agregar_conexion("Guerrero", "Michoacán", 280)

# Mostrar el grafo en formato ASCII
grafo.mostrar_grafo_ascii()


grafo.mostrar_relaciones()


print("\nRecorrido sin repetición:")
print("=" * 50)
ruta1, costo1 = grafo.recorrido_sin_repeticion("Jalisco")
print(f"Ruta: {' -> '.join(ruta1)}")
print(f"Costo total: ${costo1}")

print("\nRecorrido con repetición (al menos un estado 3 veces):")
print("=" * 50)
ruta2, costo2 = grafo.recorrido_con_repeticion("Jalisco")
print(f"Ruta: {' -> '.join(ruta2)}")
print(f"Costo total: ${costo2}")


print("\nEstadísticas del recorrido con repetición:")
print("=" * 50)
conteo = {}
for estado in ruta2:
    conteo[estado] = conteo.get(estado, 0) + 1
print("Número de visitas por estado:")
for estado, visitas in sorted(conteo.items()):
    print(f"  {estado}: {visitas} {'vez' if visitas == 1 else 'veces'}")