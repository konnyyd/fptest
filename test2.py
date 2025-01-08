print("Bienvenido, ingrese su edad")
edad = int(input())  
if edad < 12:
    print("El valor de su entrada es de $500")
    precio_entrada = 500
elif edad >= 13 and edad < 18:
    print("El valor de su entrada es de $1000")
    precio_entrada = 1000
elif edad >= 19 and edad <= 64:
    print("El valor de su entrada es de $2000")
    precio_entrada = 2000
elif edad > 65:
    print("El valor de su entrada es de $700")
    precio_entrada = 700
else:
    print("Ingrese un número válido")
    precio_entrada = 0  

if precio_entrada > 0:  
    print("¿Cuántas entradas desea?")
    cantidad_entradas = int(input())  

    total = precio_entrada * cantidad_entradas  
    print(f"El total por {cantidad_entradas} entradas es de ${total}")