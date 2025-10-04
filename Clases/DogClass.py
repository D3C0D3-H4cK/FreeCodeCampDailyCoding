class perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print(f'guau, soy {self.nombre}')
perroLadrando = perro("Juan")
perroLadrando.ladrar()
