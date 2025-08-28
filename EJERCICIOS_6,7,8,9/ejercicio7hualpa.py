#ejercicio7
exchange_rates = {
    "eur": 0.86,
    "arg": 1351,
    "colombiano": 4029
}
print("Convertir dolares a otras monedas")
usd_disponible = float(input("ingrese la cantidad de dolares a cambiar: "))

print("Monedas disponibles: eur, arg, colombiano")
moneda = input("¿A qué moneda desea cambiar? ").lower()

if moneda in exchange_rates:
    resultado = usd_disponible * exchange_rates[moneda]
    print(f"{usd_disponible} USD equivalen a {resultado:.2f} {moneda}")
else:
    print("Moneda no válida.")