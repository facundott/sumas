class Family:
    papa = 1000
    mama = 2000
    facundo = 3000
    abuelita_miguelina = 4000
    abuela_maruja = 5000
    tia_vero = 6000
    tio_luis = 7000
    tio_antonio = 8000
    tia_ruth = 9000

    @staticmethod
    def total_suma():
        total = (
            Family.papa
            + Family.mama
            + Family.facundo
            + Family.abuelita_miguelina
            + Family.abuela_maruja
            + Family.tia_vero
            + Family.tio_luis
            + Family.tio_antonio
            + Family.tia_ruth
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            Family.papa
            * Family.mama
            * Family.facundo
            * Family.abuelita_miguelina
            * Family.abuela_maruja
            * Family.tia_vero
            * Family.tio_luis
            * Family.tio_antonio
            * Family.tia_ruth
        )
        return total