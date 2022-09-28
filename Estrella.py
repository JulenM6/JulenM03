class Producte:
  def __init__(self, cost, price):
    self.__cost = cost
    self.__price = price
    
  def getGain(self):
    return self.__cost - self.__price

class Beguda:
    def __init__(self, nom):
        self.__nom = nom
        
    def getDetail(self):
        return f"Aquest objecte és {self.__nom}"
class Estrella(Beguda, Producte):
       
    def __init__(self, nom, brand, alcohol, cost, price):
        
        Beguda.__init__(self, nom)
        Producte.__init__(self,cost, price)
        self.__brand= brand
        self.__alcohol = alcohol
        
        
    def getDetail(self, text=""):
            return f"{super().getDetail()} de la marca {self.__brand} amb {self.__alcohol}"
        
        
Estrella1 = Estrella("Estrella","galicia",10,1,4)
print(Estrella1.getDetail())
print(Estrella1.getGain())