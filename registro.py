class Registro:
    __temperatura=float
    __humedad=float
    __presion=float
    def __init__(self, temperatura=0.0,humedad=0.0,presion=0.0):
        self.__temperatura= temperatura
        self.__humedad=humedad
        self.__presion=presion
    def getTemp(self):
        return self.__temperatura
    def getHum(self):
        return self.__humedad
    def getPre(self):
        return self.__presion
    def __str__(self) -> str:
        return '%s %s %s'%(self.__temperatura,self.__humedad,self.__presion)