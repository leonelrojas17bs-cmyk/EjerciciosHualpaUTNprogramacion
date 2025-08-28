#ejercicio 6
parcial1 = float(input("ingrese las califaciones de los parciales: "))
parcial2 = float(input())
parcial3 = float(input())
parcialtotal = (parcial1 + parcial2 + parcial3) / 3
examen_final = float(input("ingrese la calificacion del examen final: "))
trabajo_final = float(input("ingrese la calificacion del trabajo final: "))
nota_final = (parcialtotal * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"la nota final es de {nota_final}")