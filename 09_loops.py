#LOOPS
#while




my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    
print("La ejecucion continua")

#For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
 print(element)


my_tuple = (32, 1.80, "Hector", "Sanchez", "Hector")

for element in my_tuple:
 print(element)

my_set = {"Hector", "Sanchez", 32}

for elements in my_set:
 print(element)

my_dict = {"Nombre": "Hector", "Apellido": "Sanchez", "Edad": 32, 1: "Python"}

for elements in my_dict:
 print(element)
 if element == "Edad":
        break
else:
 print("El bucle for para diccionario ha finalizado")
        
print("La ejecucion continua")

for element in my_dict:
 print(element)
 if element == "Edad":
        continue
 print("Se ejecuta")
else:
 print("El bucle for para diccionario ha finalizado")