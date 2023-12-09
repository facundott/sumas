class CellphoneBrands:
    samsung = 1000
    huawei = 2000
    iphone = 3000
    oppo = 4000
    vivo = 5000
    xiaomi = 6000
    oneplus = 7000
    nokia = 8000
    sony = 9000
    lg = 10000
    motorola = 11000
    htc = 12000

    @staticmethod
    def total_suma():
        total = (
            + CellphoneBrands.samsung
            + CellphoneBrands.huawei
            + CellphoneBrands.iphone
            + CellphoneBrands.oppo
            + CellphoneBrands.vivo
            + CellphoneBrands.xiaomi
            + CellphoneBrands.oneplus
            + CellphoneBrands.nokia
            + CellphoneBrands.sony
            + CellphoneBrands.lg
            + CellphoneBrands.motorola
            + CellphoneBrands.htc 
        )
        return total

    @staticmethod
    def total_multiplicacion():
        total = (
            CellphoneBrands.samsung
            * CellphoneBrands.huawei
            * CellphoneBrands.iphone
            * CellphoneBrands.oppo
            * CellphoneBrands.vivo
            * CellphoneBrands.xiaomi
            * CellphoneBrands.oneplus
            * CellphoneBrands.nokia
            * CellphoneBrands.sony
            * CellphoneBrands.lg
            * CellphoneBrands.motorola
            * CellphoneBrands.htc 
        )
        return total
