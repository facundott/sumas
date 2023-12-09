class Foods:
    pizza = 100
    hamburguesa = 200
    hotdog = 300
    fideos = 400
    ensalada = 500
    arroz = 600
    carne = 700
    filete_de_pollo = 800
    filete_de_atun = 900

    @staticmethod
    def total_suma():
        total = (
            Foods.pizza
            + Foods.hamburguesa
            + Foods.hotdog
            + Foods.fideos
            + Foods.ensalada
            + Foods.arroz
            + Foods.carne
            + Foods.filete_de_pollo
            + Foods.filete_de_atun
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            Foods.pizza
            * Foods.hamburguesa
            * Foods.hotdog
            * Foods.fideos
            * Foods.ensalada
            * Foods.arroz
            * Foods.carne
            * Foods.filete_de_pollo
            * Foods.filete_de_atun
        )
        return total
