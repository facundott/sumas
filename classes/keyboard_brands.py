class KeyboardBrands:
    teros = 1000
    razer = 2000
    logitech = 3000
    genius = 4000
    microsoft = 5000
    apple = 6000
    hp = 8000
    asus = 9000
    acer = 10000
    coller_master = 11000

    @staticmethod
    def total_suma():
        total = (
            KeyboardBrands.teros
            + KeyboardBrands.razer
            + KeyboardBrands.logitech
            + KeyboardBrands.genius
            + KeyboardBrands.microsoft
            + KeyboardBrands.apple
            + KeyboardBrands.hp
            + KeyboardBrands.asus
            + KeyboardBrands.acer
            + KeyboardBrands.coller_master
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            KeyboardBrands.teros
            * KeyboardBrands.razer
            * KeyboardBrands.logitech
            * KeyboardBrands.genius
            * KeyboardBrands.microsoft
            * KeyboardBrands.apple
            * KeyboardBrands.hp
            * KeyboardBrands.asus
            * KeyboardBrands.acer
            * KeyboardBrands.coller_master
        )
        return total