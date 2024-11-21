nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (Mujer o Hombre)? ")
if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)