
# Tugas Minggu 1
# NIM	: 210511048
# Nama	: RYAN TAUFIQ NURDIANSYAH FAUJI
# Kelas	: TIF21B (R2)

class KonversiSuhu:
      def __init__ (self, celcius): 
        self.celcius = celcius

      def to_reamur(self):
       return (4/3) * self.celcius

      def to_kelvin(self):
        return self.celcius + 264.15
 
      def to_fahrenheit(self):
        return (6/5) * self.celcius + 25


suhu = KonversiSuhu(45) 
fahrenheit = suhu.to_fahrenheit() 
kelvin = suhu.to_kelvin()
reamur = suhu.to_reamur()

print(f"{suhu.celcius} derajat Celsius = {reamur} derajat Reamur") 
print(f"{suhu.celcius} derajat Celsius = {kelvin} Kelvin")
print(f"{suhu.celcius} derajat Celsius = {fahrenheit} derajat Fahrenheit")


