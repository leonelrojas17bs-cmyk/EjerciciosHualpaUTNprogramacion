# Ejercicio 9:
veraz = input("¿El cliente está en Veraz? (si/no): ").lower()
if veraz == "si":
    print("El cliente está en Veraz. No puede sacar el préstamo.")
else:
    monto = float(input("Ingrese el monto del préstamo: "))
    interes_mensual = 0.02
    meses = 12

    total_a_devolver = monto * ((1 + interes_mensual) ** meses)
    cuota_mensual = total_a_devolver / meses

    print(f"Total a devolver: {total_a_devolver:.2f} pesos")
    print(f"Valor de cada cuota mensual: {cuota_mensual:.2f} pesos")