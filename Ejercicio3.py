# Clase Punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def impresion(self):
        return f"({self.x}, {self.y})"


# Clase Linea
class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def impresion(self):
        return f"Línea desde {self._punto_a.impresion()} hasta {self._punto_b.impresion()}"
    
p1 = Punto(0, 0)
p2 = Punto(3, 4)

linea = Linea(p1, p2)
print(linea.impresion())  

linea.mueve_derecha(2)
print(linea.impresion())  

linea.mueve_arriba(1)
print(linea.impresion()) 