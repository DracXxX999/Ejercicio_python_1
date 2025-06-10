#Contador
print ("Contador")
for numero in range (4):
    print (numero)
#Nombres
print ("\n Recorriendo un string")
nombre = "Marquiño"
for letra in nombre:
    print(letra)
#Multiplicación 
tabla = int(input("Ingresa cualquier número: "))
print(f"tabla del {tabla}")
for i  in range (1, 11):
    resultado = tabla * i 
    print(f"{tabla} * {i} = {resultado}")
#While
contador = 0
print("\nBucle while")
while contador < 4:
    print(f"contador es: {contador}") 
    contador = contador + 1
print("¡Bulce While terminado! ")
#Rectángulo
b = 10
h = 5
a = b * h
print(f"El área de un rectángulo es= {a}")
#Rectángulo 2
base = 12
altura = 2
área = base * altura
print (f"El área de un rectángulo es: {área}")

def mostrar_area_rectangulo (base, altura):
    area = base * altura
    print(f"El área del rectánfulo {base} * {altura} = {area}")
mostrar_area_rectangulo (10, 4)