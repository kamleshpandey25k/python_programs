class Car:
  def __init__(self, brand,model):
      self.model=model
      self.brand=brand
  def __str__(self):
    return f"{self.model} {self.brand}"

mycar=Car("Tata","Nexon")
print(mycar.brand)
print(mycar.model)
print(mycar)