class DetergentBrands:
    ace = 1000
    ariel = 2000
    patito = 3000
    marsella = 4000
    bolivar = 5000
    ña_pancha = 6000
    sapolio = 7000
    opal = 8000

    @staticmethod
    def total_suma():
        total = (
            DetergentBrands.ace
            + DetergentBrands.ariel
            + DetergentBrands.patito
            + DetergentBrands.marsella
            + DetergentBrands.bolivar
            + DetergentBrands.ña_pancha
            + DetergentBrands.sapolio
            + DetergentBrands.opal
        )
        return total
    
    @staticmethod
    def total_multiplicacion():
        total = (
            DetergentBrands.ace
            * DetergentBrands.ariel
            * DetergentBrands.patito
            * DetergentBrands.marsella
            * DetergentBrands.bolivar
            * DetergentBrands.ña_pancha
            * DetergentBrands.sapolio
            * DetergentBrands.opal
        )
        return total
