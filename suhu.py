print("Program Konversi Suhu ekorkode.com")

suhu = input("Masukan suhu? (Misal: 30C, 20F, 21K, 44R): ")
drjt = int(suhu[:-1])
inputan = suhu[-1]

if inputan.upper() == "C":
  hasil1 = float((9 * drjt) / 5 + 32)
  hasil2 = float(drjt + 273.15)
  hasil3 = float(4/5 * drjt)
  jenisX = "Celcius"
  jenis1 = "Fahrenheit"
  jenis2 = "Kelvin"
  jenis3 = "Reamur"

elif inputan.upper() == "F":
  hasil1 = float((drjt - 32) * 5 / 9)
  hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
  hasil3 = float(4/9 * (drjt-32))
  jenisX = "Fahrenheit"
  jenis1 = "Celsius"
  jenis2 = "Kelvin"
  jenis3 = "Reamur"

elif inputan.upper() == "K":
  hasil1 = float(drjt - 273.15)
  hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
  hasil3 = float(4/5 * (drjt-273))
  jenisX = "Kelvin"
  jenis1 = "Celcius"
  jenis2 = "Fahrenheit"
  jenis3 = "Reamur"