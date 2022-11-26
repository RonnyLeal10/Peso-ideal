peso=float(input("O seu peso em kg: "))
Altura=float(input("A sua altura em metros: "))
IMG=peso/(Altura**2)
if IMG < 18.5:
    print("Abaixo de peso")
elif IMG >18.5 and IMG <=25:
    print("Peso ideal")
elif IMG >25 and IMG<=30:
    print("Sobrepeso")
elif IMG >30 and IMG<=40:
    print("Obesidade")
else :
    print("Obesidade morbida")

