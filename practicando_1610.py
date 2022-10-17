menu = """
Bienvenido al conversor de monedas, de dolar 
a la moneda latinoamericana que eligas
 💸💱💲

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Uruguayos
4- Peso Boliviano
5- Guarani
6- Peso Chileno
7- Sol Peruano
8- Real
9- Bolivar
10- Dolar Ecuatoriano
11- Peso Mexicano 
12- Dolar Canadiense
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4698
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 290
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos uruguayos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 40
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 4:
    pesos = input("¿Cuántos pesos bolivianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 6.91
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 5:
    pesos = input("¿Cuántos guaranies paraguayos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 7158
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 6:
    pesos = input("¿Cuántos pesos chilenos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 962
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 7:
    pesos = input("¿Cuántos soles peruanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3.96
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 8:
    pesos = input("¿Cuántos reales brasileros tienes?: ")
    pesos = float(pesos)
    valor_dolar = 6
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 9:
    pesos = input("¿Cuántos bolivares tienes?: ")
    pesos = float(pesos)
    valor_dolar = 8.26
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 10:
    pesos = input("¿Cuántos dolares ecuatorianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 1
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 11:
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20.03
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 12:
    pesos = input("¿Cuántos dolares canadienses tienes?: ")
    pesos = float(pesos)
    valor_dolar = 1.38
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

