
from abc import ABC, abstractmethod
class IProduct(ABC):
    @abstractmethod
    def ShipFrom(self):
        pass

class ProductA(IProduct):
    def ShipFrom(self):
        return " from South Aftrica"

class ProductB(IProduct):
    def ShipFrom(self):
        return " from Spain"

class DefaultProduct(IProduct):
    def ShipFrom(self):
        return "not available"



class ProductFactory:
    def Create(self, month):
        if month>=4 and month<=11:
            return ProductA()
        elif month ==1 or month ==2 or month == 12:
            return ProductB()
        else:
            return DefaultProduct()


if __name__ == "__main__":
    factory = ProductFactory()
    for i in range(1,13):
        product = factory.Create(i)
        print(f"Avacados {product.ShipFrom()}")