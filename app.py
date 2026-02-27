# app.py

import calculator

def menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Hasta luego")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", calculator.sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", calculator.restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", calculator.multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", calculator.dividir(num1, num2))

    except ValueError as e:
        print(e)