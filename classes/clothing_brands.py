class ClothingBrands:
    urb = 1000
    nike = 2000
    adidas = 3000
    puma = 4000
    reebok = 5000
    converse = 6000
    guest = 7000
    prada = 8000

    @staticmethod
    def total_suma():
        total = (
            ClothingBrands.urb
            + ClothingBrands.nike
            + ClothingBrands.adidas
            + ClothingBrands.puma
            + ClothingBrands.reebok
            + ClothingBrands.converse
            + ClothingBrands.guest
            + ClothingBrands.prada
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            ClothingBrands.urb
            * ClothingBrands.nike
            * ClothingBrands.adidas
            * ClothingBrands.puma
            * ClothingBrands.reebok
            * ClothingBrands.converse
            * ClothingBrands.guest
            * ClothingBrands.prada
        )
        return total