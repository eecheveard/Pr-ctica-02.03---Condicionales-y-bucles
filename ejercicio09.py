n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for y in range(i, 0, -2):
        print(y, end=" ")
    print("")