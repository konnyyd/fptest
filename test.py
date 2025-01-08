# nombre = "Constanza Diaz"
# edad = 23
# print("mi nombre es", nombre)
# print("mi edad es", edad)

# num1 = 0
# num2 = 0
#---------------------------------------------
# print ("ingrese un numero")
# num1 = int(input())
# print ("ingrese un numero")
# num2 = int(input())
# print("el resultado es", num1*num2)
#---------------------------------------------
# print ("ingrese un numero")
# num1 = int(input())
# if num1 >= 18:
#     print ("es mayor de edad")
# else:
#     print ("es menor de edad") 
#--------------------------------------------
# print ("ingrese su nota")
# num1 = int(input())
# print ("ingrese su segunda nota")
# num2 = int(input())
# print ("ingrese su tercera nota")
# num3 = int(input())
# print((num1+num2+num3)/3)
#--------------------------------------------

print ("bienvenido, ingrese su edad")
edad = int(input())
if edad < 12  : 
    monto=500
    print("cuentas entradas desea?")
    cantidad=int(input())
    t=monto * cantidad
    print ("el valor de su entrada es de ",t )
elif edad >13 and edad <18  :
    monto=1000
    print("cuentas entradas desea?")
    cantidad=int(input())
    t=monto * cantidad
    print ("el valor de su entrada es de",t)
elif edad >19 and edad <=64:
    monto=2000
    print("cuentas entradas desea?")
    cantidad=int(input())
    t=monto * cantidad
    print ("el valor de su entrada es de", t)
elif edad >65:
    monto=700
    print("cuentas entradas desea?")
    cantidad=int(input())
    t=monto * cantidad
    print ("el valor de su entrada es de", t)
else:
    print("el total es")


