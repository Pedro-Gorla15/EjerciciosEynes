class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio del círculo debe ser mayor que cero")
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.14 * self.radio

    def set_radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio del círculo debe ser mayor que cero")
        self.radio = radio

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El valor debe ser mayor a cero")


circulo = Circulo (5)

area = circulo.area()
perimetro = circulo.perimetro()

print("Área: ", area)
print("Perímetro: ", perimetro)

print(circulo)