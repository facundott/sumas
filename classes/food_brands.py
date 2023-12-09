class FoodBrands:
    dominos_pizza = 1000
    pizza_brava = 2000
    pizza_hut = 3000
    mega_pollo = 4000
    mcdonalds = 5000
    burger_king = 6000
    subway = 7000
    taco_bell = 8000
    kfc = 9000
    papa_johns = 10000

    @staticmethod
    def total_suma():
        total = (
            FoodBrands.dominos_pizza
            + FoodBrands.pizza_brava
            + FoodBrands.pizza_hut
            + FoodBrands.mega_pollo
            + FoodBrands.mcdonalds
            + FoodBrands.burger_king
            + FoodBrands.subway
            + FoodBrands.taco_bell
            + FoodBrands.kfc
            + FoodBrands.papa_johns
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            FoodBrands.dominos_pizza
            * FoodBrands.pizza_brava
            * FoodBrands.pizza_hut
            * FoodBrands.mega_pollo
            * FoodBrands.mcdonalds
            * FoodBrands.burger_king
            * FoodBrands.subway
            * FoodBrands.taco_bell
            * FoodBrands.kfc
            * FoodBrands.papa_johns
        )
        return total