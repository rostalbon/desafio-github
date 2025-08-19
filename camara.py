class Camara:
    def __init__(self, marca, modelo, almacenamiento, fotos = 0, ocupado = 0):
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__ocupado = ocupado
        self.__fotos = fotos
    def set_marca(self, marca):
        self.__marca = marca
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento
    def get_fotos(self):
        return self.__fotos
    def get_almacenamiento(self):
        return self.__almacenamiento
    def get_ocupado(self):
        return self.__ocupado
    def __add__(self, fotos):
        self.__fotos = self.__fotos + fotos
        self.__ocupado = self.__ocupado + fotos * 5
    def __sub__(self, fotos):
        self.__fotos = self.__fotos - fotos
        self.__ocupado = self.__ocupado - fotos * 5
    def __str__(self):
        return f"Marca: {self.__marca}\nModelo: {self.__modelo}\nAlmacenamiento: {self.__almacenamiento} MB (Ocupado: {self.__ocupado} MB)\nFotos: {self.__fotos}"