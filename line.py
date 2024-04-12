import math
def line():

    A = float(input("Ingrese el coeficiente A:"))
    B = float(input("Ingrese el coeficiente B:"))
    X1 = float(input("Ingrese el coeficiente X1:"))
    X2 = float(input("Ingrese el coeficiente X2:"))

    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print("\n" + "Para la siguiente ecuación:")
    print("\t" + "Y = " + str(A)+"X" " + "+ str(B))

    Y1 = (A*X1+B)
    Y2 = (A*X2+B)

    p1 = (X1 , Y1)
    p2 = (X2, Y2)

    print("\n" + "Dados los siguientes puntos:")
    print(f"\tP1 {p1}")
    print(f"\tP2 {p2}")

    distancia = (math.dist(p1,p2))

    print(f"\nLa distancia entre ellos es: {distancia}")
