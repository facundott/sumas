class Transports:
    carro = 5000
    coaster = 10000
    moto = 3000
    bicicleta = 500
    autobus = 2000
    taxi = 1000
    avion = 100000
    helicóptero = 20000
    barco = 30000
    nave_espacial = 50000

    @staticmethod
    def total_suma():
        total = (
            Transports.carro
            + Transports.coaster
            + Transports.moto
            + Transports.bicicleta
            + Transports.autobus
            + Transports.taxi
            + Transports.avion
            + Transports.helicóptero
            + Transports.barco
            + Transports.nave_espacial            
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            Transports.carro
            * Transports.coaster
            * Transports.moto
            * Transports.bicicleta
            * Transports.autobus
            * Transports.taxi
            * Transports.avion
            * Transports.helicóptero
            * Transports.barco
            * Transports.nave_espacial            
        )
        return total