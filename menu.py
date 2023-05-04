from registro import Registro
class Menu:
    __opcion= int
    def __init__(self,opcion=4):
        self.__opcion=opcion
    def opciones(self,lista):
        while self.__opcion!=0:
            print('\n1 - Mostrar dia y hora de menor y mayor valor')
            print('2 - Indicar temperatura promedio mensual por cada hora')
            print('3 - Listar valores valores de las tres varriables para cada hora')
            print('0 - Salir\n')
            self.__opcion=int(input('Ingrese la opcion a ejecutar: '))
            if self.__opcion==1:
                print('Inciso 1\n')

                print('Temperatura')
                print('\nMENOR')
                lista.minimoTemp()
                print('\nMAYOR')
                lista.maximoTemp()

                print('\nHumedad')
                print('\nMENOR')
                lista.minimoHum()
                print('\nMAYOR')
                lista.maximoHum()

                print('\nPresion')
                print('\nMENOR')
                lista.minimoPre()
                print('\nMAYOR')
                lista.maximoPre()

            elif self.__opcion==2:
                print('\nInciso 2\n')
                lista.promTempMensual()
            elif self.__opcion==3:
                print('\nInciso 3\n')
                dia=int(input('Ingrese numero de dia: \n'))
                lista.listarValores(dia)
            else:
                print('\nHa salido del sistema')