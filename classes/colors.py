class Colors:
    rojo = 4000
    azul = 2000
    verde = 6000
    amarillo = 3000
    anaranjado = 1000
    morado = 500
    blanco = 100
    negro = 50
    gris = 10
    celeste = 8000
    violeta = 7000
    marron = 6000
    dorado = 5000
    plateado = 4000
    turquesa = 3000

    
    @staticmethod
    def total_suma():
        total = (
            Colors.rojo
            + Colors.azul
            + Colors.verde
            + Colors.amarillo
            + Colors.anaranjado
            + Colors.morado
            + Colors.blanco
            + Colors.negro
            + Colors.gris
            + Colors.celeste
            + Colors.violeta
            + Colors.marron
            + Colors.dorado
            + Colors.plateado
            + Colors.turquesa
        )
        return total
    
    @staticmethod
    def total_multiplicacion():
        total = (
            Colors.rojo
            * Colors.azul
            * Colors.verde
            * Colors.amarillo
            * Colors.anaranjado
            * Colors.morado
            * Colors.blanco
            * Colors.negro
            * Colors.gris
            * Colors.celeste
            * Colors.violeta
            * Colors.marron
            * Colors.dorado
            * Colors.plateado
            * Colors.turquesa
        )
        return total
