from registro import Registro
import csv
class GestorRegistros:
    __listaRegistros=[]
    def __init__(self):
        self.__listaRegistros=[None for i in range(3)]
        for i in range(3):
            self.__listaRegistros[i]=[] * 5

    def agregarRegistro(self,dia,hora,registro):
        self.__listaRegistros[dia-1].append(registro)

    def leerArchivo(self):
        file = open('archivo.csv')
        reader= csv.reader(file,delimiter=',')
        for fila in reader:
            dia= int(fila[0])
            hora=int(fila[1])
            temp=float(fila[2])
            hum=float(fila[3])
            pre=float(fila[4])
            unRegistro= Registro(temp,hum,pre)
            self.agregarRegistro(dia,hora,unRegistro)

    def minimoTemp(self):
        m=float(self.__listaRegistros[0][0].getTemp())
        for i in range(3):
            for j in range(2):
                if m>float(self.__listaRegistros[i][j].getTemp()):
                    m=float(self.__listaRegistros[i][j].getTemp())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getTemp()):
                    print('Dia de menor temperatura: %s'%(i+1))
                    print('Hora de menor temperatura: %s'%(j))
    def maximoTemp(self):
        m=float(self.__listaRegistros[0][0].getTemp())
        for i in range(3):
            for j in range(2):
                if m<float(self.__listaRegistros[i][j].getTemp()):
                    m=float(self.__listaRegistros[i][j].getTemp())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getTemp()):
                    print('Dia de mayor temperatura: %s'%(i+1))
                    print('Hora de mayor temperatura: %s'%(j))


    def minimoHum(self):
        m=float(self.__listaRegistros[0][0].getHum())
        for i in range(3):
            for j in range(2):
                if m>float(self.__listaRegistros[i][j].getHum()):
                    m=float(self.__listaRegistros[i][j].getHum())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getHum()):
                    print('Dia de menor humedad: %s'%(i+1))
                    print('Hora de menor humedad: %s'%(j))
    def maximoHum(self):
        m=float(self.__listaRegistros[0][0].getHum())
        for i in range(3):
            for j in range(2):
                if m<float(self.__listaRegistros[i][j].getHum()):
                    m=float(self.__listaRegistros[i][j].getHum())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getHum()):
                    print('Dia de mayor humedad: %s'%(i+1))
                    print('Hora de mayor humedad: %s'%(j))


    def minimoPre(self):
        m=float(self.__listaRegistros[0][0].getPre())
        for i in range(3):
            for j in range(2):
                if m>float(self.__listaRegistros[i][j].getPre()):
                    m=float(self.__listaRegistros[i][j].getPre())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getPre()):
                    print('Dia de menor presion: %s'%(i+1))
                    print('Hora de menor presion: %s'%(j))
    def maximoPre(self):
        m=float(self.__listaRegistros[0][0].getPre())
        for i in range(3):
            for j in range(2):
                if m<float(self.__listaRegistros[i][j].getPre()):
                    m=float(self.__listaRegistros[i][j].getPre())
        for i in range(3):
            for j in range(2):
                if m==float(self.__listaRegistros[i][j].getPre()):
                    print('Dia de mayor presion: %s'%(i+1))
                    print('Hora de mayor presion: %s'%(j))


    def promTempMensual(self):
        tot=[0,0]
        for i in range(2):
            for j in range(3):
                tot[i]+=float(self.__listaRegistros[j][i].getTemp())
            print('Temperatura promedio mensual de la hora %s: %.2f\n'%(i,tot[i]/3))
    def listarValores(self,dia):
        print('Dia elegido %d'%(dia))
        print('\nHora    Temperatura     Humedad     Presion')
        for i in range(2):
            print('%d           %.2f         %.2f       %.2f'%(i,self.__listaRegistros[dia-1][i].getTemp(),self.__listaRegistros[dia-1][i].getHum(),self.__listaRegistros[dia-1][i].getPre()))

    def __str__(self):
        s=''
        for i in range(3):
            for j in range(2):
                s+=str(self.__listaRegistros[i][j]) + '\n'
        return s
        
    
