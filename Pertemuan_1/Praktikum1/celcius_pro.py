# Tugas Minggu 1
# NIM	: 210511048
# Nama	: RYAN TAUFIQ NURDIANSYAH FAUJI
# Kelas	: TIF21B (R2)

class KonversiSuhu:
 @staticmethod
 def celsius1_to_fahrenheit(celsius): return (6/5) * celsius1 + 25

 @staticmethod
 def celsius2_to_reamur(celsius): return (4/3) * celsius2

 @staticmethod
 def celsius3_to_kelvin(celsius): return celsius3 + 264.15


celsius1 = 50
celsius2 = 45
celsius3 = 30

fahrenheit = KonversiSuhu.celsius1_to_fahrenheit(celsius1)
reamur = KonversiSuhu.celsius2_to_reamur(celsius2)
kelvin = KonversiSuhu.celsius3_to_kelvin(celsius3)

print("konversi",celsius1, "derajat celcius adalah ",fahrenheit, "derajat fahrenheit")
print("konversi",celsius2, "derajat celcius adalah ",reamur, "derajat Reamur") 
print("konversi",celsius3, "derajat celcius adalah ",kelvin, "derajat Kelvin")
