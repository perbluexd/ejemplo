listaCiudades = []

var = int(input("che pa cuantos paises tienes: "))

for i in range(var):
    ciudad = [
             int(input("escribe el número de ciudad: ")),
             str(input("escribe el nombre de la ciudad: ")),
             int(input("escribe la población de la ciudad: "))
           ]
    registrado = False
    for city in listaCiudades:
        if (city[0] == ciudad[0]):
            registrado = True
            break
    if (registrado):
        print("ya se encuentra")
    else: 
        listaCiudades.append(ciudad)

print(listaCiudades)
print("todo correcto maestro")
print("agregando para probar waaa")