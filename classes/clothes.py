class Clothes:
    polo = 1000
    camisa = 2000
    pantalon = 3000
    zapatillas = 4000
    calcetines = 5000
    sombrero = 6000
    gorro = 7000
    guantes = 8000
    botas = 9000
    chaleco = 10000
    pijama = 11000
    short = 12000
    calzoncillo = 13000
    chaqueta = 14000
    camiseta = 15000
    bermuda = 16000

    @staticmethod
    def total_suma():
        total = (
            Clothes.polo
            + Clothes.camisa
            + Clothes.pantalon
            + Clothes.zapatillas
            + Clothes.calcetines
            + Clothes.sombrero
            + Clothes.gorro
            + Clothes.guantes
            + Clothes.botas
            + Clothes.chaleco
            + Clothes.pijama
            + Clothes.short
            + Clothes.calzoncillo
            + Clothes.chaqueta
            + Clothes.camiseta
            + Clothes.bermuda
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            Clothes.polo
            * Clothes.camisa
            * Clothes.pantalon
            * Clothes.zapatillas
            * Clothes.calcetines
            * Clothes.sombrero
            * Clothes.gorro
            * Clothes.guantes
            * Clothes.botas
            * Clothes.chaleco
            * Clothes.pijama
            * Clothes.short
            * Clothes.calzoncillo
            * Clothes.chaqueta
            * Clothes.camiseta
            * Clothes.bermuda
        )
        return total
