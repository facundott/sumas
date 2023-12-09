class Animals:
    perro = 4000
    gato = 2000
    lechuloma = 6000
    cerdo = 3000
    gallina = 1000
    tortuga = 500
    pato = 100
    pollo = 100000
    caballo = 20000
    raton = 50
    toro = 5000


    @staticmethod
    def total_suma():
        total_suma = (
            Animals.perro
            + Animals.gato
            + Animals.lechuloma
            + Animals.lechuloma
            + Animals.cerdo
            + Animals.gallina
            + Animals.tortuga
            + Animals.pato
            + Animals.pollo
            + Animals.caballo
            + Animals.raton
            + Animals.toro
        )
        return total_suma

    @staticmethod
    def total_multiplicacion():
        total_suma = (
            Animals.perro
            * Animals.gato
            * Animals.lechuloma
            * Animals.lechuloma
            * Animals.cerdo
            * Animals.gallina
            * Animals.tortuga
            * Animals.pato
            * Animals.pollo
            * Animals.caballo
            * Animals.raton
            * Animals.toro
        )
        return total_suma
