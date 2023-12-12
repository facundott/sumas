class Fruits:
    manzana = 1000
    platano = 2000
    pera = 3000
    sandia = 4000
    naranja = 5000
    mango = 6000
    uva = 7000
    melon = 8000
    kiwi = 9000
    papaya = 10000
    mandarina = 11000

    @staticmethod
    def total_suma():
        total = (
            Fruits.manzana
            + Fruits.platano
            + Fruits.pera
            + Fruits.sandia
            + Fruits.naranja
            + Fruits.mango
            + Fruits.uva
            + Fruits.melon
            + Fruits.kiwi
            + Fruits.papaya
            + Fruits.mandarina
        )
        return total
