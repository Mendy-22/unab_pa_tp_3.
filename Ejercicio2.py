class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto (-self.x, -self.y)

p1 = Punto(3, 4)
print(p1.impresion())        
print(p1.eje_x())            
print(p1.eje_y())            
print(p1.opuesto().impresion())  