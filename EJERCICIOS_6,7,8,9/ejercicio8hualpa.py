distancia = float(input("ingrese la distancia en km: "))
precio = float(input("ingrese el precio por litro de gasolina: "))
litros_necesarios = (distancia / 100) * 8
print(f"Se necesitan {litros_necesarios:.2f} litros de gasolina para el viaje.")
costo_total = litros_necesarios * precio
print(f"El costo total del viaje es de {costo_total:.2f} pesos")
velocidad_promedio = 90  # km/h
tiempo = distancia / velocidad_promedio
print(f"El tiempo estimado de viaje es de {tiempo:.2f} horas")