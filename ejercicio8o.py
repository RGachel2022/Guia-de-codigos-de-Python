print("Pon un numero cualquiera")
num = int(input("Introduce el número: "))

if num % 3 == 0 and num % 5 == 0:
    print("El número es múltiplo de 3 y 5")
elif num % 3 == 0:
    print("El número es múltiplo de 3 pero no de 5")
elif num % 5 == 0:
    print("El número es múltiplo de 5 pero no de 3")
else:
    print("El número no es múltiplo de 3 ni de 5")
