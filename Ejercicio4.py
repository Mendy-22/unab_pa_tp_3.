class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        
c1 = Cancion("Imagine", "John Lennon")

print(c1.get_titulo())  
print(c1.get_autor())  

c1.set_titulo("Hey Jude")
c1.set_autor("The Beatles")

print(c1.get_titulo())  
print(c1.get_autor())  