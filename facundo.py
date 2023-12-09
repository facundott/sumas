from classes.animals import Animals
from classes.transports import Transports
from classes.colors import Colors
from classes.letters import Letters
from classes.foods import Foods
from classes.drinks import Drinks
from classes.car_brands import CarBrands
from classes.food_brands import FoodBrands
from classes.clothes import Clothes
from classes.family import Family
from classes.keyboards import keyboards
from classes.beverage_brands import BeverageBrands
from classes.clothing_brands import ClothingBrands
from classes.cellphone_brands import CellphoneBrands


respuesta = (
    Animals.total_multiplicacion()
    * Transports.total_multiplicacion()
    * Colors.total_multiplicacion()
    * Letters.total_multiplicacion()
    * Foods.total_multiplicacion()
    * Drinks.total_multiplicacion()
    * CarBrands.total_multiplicacion()
    * FoodBrands.total_multiplicacion()
    * Clothes.total_multiplicacion()
    * Family.total_multiplicacion()
    * keyboards.total_multiplicacion()
    * BeverageBrands.total_multiplicacion()
    * ClothingBrands.total_multiplicacion()
    * CellphoneBrands.total_multiplicacion()
)

print()
print("*" * 50)
print("El resultado de todo es:")
print(respuesta)
print()
print("El resultado de 4k + 2k es:")
resultado = "4k" + "2k"
print(resultado)
print("*" * 50)
