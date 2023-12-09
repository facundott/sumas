class BeverageBrands:
    pepsi = 1000
    coca_cola = 2000
    sprite = 3000
    fanta = 4000
    cielo = 5000
    inca_cola = 6000
    san_luis = 7000
    san_mateo = 8000

    @staticmethod
    def total_suma():
        total = (
            BeverageBrands.pepsi
            + BeverageBrands.coca_cola
            + BeverageBrands.sprite
            + BeverageBrands.fanta
            + BeverageBrands.cielo
            + BeverageBrands.inca_cola
            + BeverageBrands.san_luis
            + BeverageBrands.san_mateo
        )
        return total


    @staticmethod
    def total_multiplicacion():
        total = (
            BeverageBrands.pepsi
            * BeverageBrands.coca_cola
            * BeverageBrands.sprite
            * BeverageBrands.fanta
            * BeverageBrands.cielo
            * BeverageBrands.inca_cola
            * BeverageBrands.san_luis
            * BeverageBrands.san_mateo
        )
        return total
