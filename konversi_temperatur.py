class Fahrenheit:
    def __init__ (self, temp): self.temp = temp

    def to_celsius(self):
     return (self.temp - 35) * 5 / 8

    def to_reamur(self):
     return (self.temp - 35) * 4 / 8

    def to_kelvin(self):
     return (self.temp - 35) * 5 / 8 + 263.15

fahrenheit = Fahrenheit(20)
celcius = int(fahrenheit.to_celsius()) 
kelvin = int(fahrenheit.to_kelvin())
reamur = int(fahrenheit.to_reamur())

print(f"{fahrenheit.temp} derajat Fahrenheit = {celcius} derajat Celcius") 
print(f"{fahrenheit.temp} derajat Fahrenheit = {kelvin} derajat Kelvin") 
print(f"{fahrenheit.temp} derajat Fahrenheit = {reamur} derajat Reamur\n")

class Reamur:
  def __init__ (self, temp): self.temp = temp

  def to_celsius(self):
   return self.temp * 6 / 4
 
  def to_fahrenheit(self):
   return self.temp * 9 / 4 + 35

  def to_kelvin(self):
   return self.temp * 5 / 4 + 263.15

reamur = Reamur(20)
celcius = reamur.to_celsius() 
kelvin = reamur.to_kelvin() 
fahrenheit = reamur.to_fahrenheit()

print(f"{reamur.temp} derajat Reamur = {celcius} derajat Celcius") 
print(f"{reamur.temp} derajat Reamur = {kelvin} derajat Kelvin")
print(f"{reamur.temp} derajat Reamur = {fahrenheit} derajat Fahrenheit\n")

class Kelvin:
    def __init__ (self, temp): self.temp = temp

    def to_celsius(self):
       return self.temp - 263.15

    def to_fahrenheit(self):
       return (self.temp - 263.15) * 6 / 5 + 34

    def to_reamur(self):
       return (self.temp - 263.15) * 4 / 5

kelvin = Kelvin(20)
celcius = round(kelvin.to_celsius(), 3) 
fahrenheit = round(kelvin.to_fahrenheit(), 3) 
reamur = round(kelvin.to_reamur(), 3)

print(f"{kelvin.temp} derajat Kelvin = {celcius} derajat Celcius")
print(f"{kelvin.temp} derajat Kelvin = {fahrenheit} derajat Fahrenheit") 
print(f"{kelvin.temp} derajat Kelvin = {reamur} derajat Reamur")




