from registro import Registro
from menu import Menu
from gestorRegistros import GestorRegistros
import csv
def test():
    gestor= GestorRegistros()
    gestor.leerArchivo()
    print(gestor)
    print('\nPUNTO 3\n')
    menu= Menu()
    menu.opciones(gestor)
    
if __name__ == '__main__':
    test()