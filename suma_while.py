print("------------ suma de los n ---------------")
print("---------- primeros números --------------")
print("---------- enteros positivos -------------")

n = int(input("Digite los n primeros números a sumar: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1
else:
    print("La suma de los " + str(n) + "primeros números es: "+ str(sum))