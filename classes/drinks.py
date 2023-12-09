class Drinks:
    cerveza = 1000
    vino = 2000
    agua = 3000
    agua_mineral = 4000
    gaseosa = 5000
    jugo_de_naranja = 6000
    cafe = 7000
    agua_de_anis = 8000
    agua_de_manzanilla = 9000
    agua_de_ecco = 10000
    quaker = 11000

    @staticmethod
    def total_suma():
        total = (
            Drinks.cerveza
            + Drinks.vino
            + Drinks.agua
            + Drinks.agua_mineral
            + Drinks.gaseosa
            + Drinks.jugo_de_naranja
            + Drinks.cafe
            + Drinks.agua_de_anis
            + Drinks.agua_de_manzanilla
            + Drinks.agua_de_ecco
            + Drinks.quaker
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            Drinks.cerveza
            * Drinks.vino
            * Drinks.agua
            * Drinks.agua_mineral
            * Drinks.gaseosa
            * Drinks.jugo_de_naranja
            * Drinks.cafe
            * Drinks.agua_de_anis
            * Drinks.agua_de_manzanilla
            * Drinks.agua_de_ecco
            * Drinks.quaker
        )
        return total