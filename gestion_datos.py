
import datetime
import os

historial = []
nombre_archivo = "registro_velocidades.csv"
archivo_existe = os.path.exists(nombre_archivo)

def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio][1] == objetivo:
            return medio
        elif lista[medio][1] > objetivo:
            alto = medio - 1
        else:
            bajo = medio + 1
    return -1


def kmh_a_mph(kmh):
    if kmh < 0:
        return None
    return kmh * 0.62 

while True:
    kmh = int(input("Velocidad de su vehículo:"))
    millas = kmh_a_mph(kmh)
    if kmh == 0:
        break

    if millas == None:
        print("Valocidad no válida")
        continue
    else:
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historial.append([ahora, kmh, f"{millas:.2f}"])
        print(f"Registrado: {millas} mph")

if not historial:
    print("Lista vacía.")
else:
    for item in historial:
        print(f"{item}")
    
    with open(nombre_archivo, "a") as archivo:
        if not archivo_existe:
            #archivo.write("sep=;\n")
            archivo.write("Fecha;KMH;MPH\n")

        archivo.write("\n--Velocidades--\n")
        for data in historial:
            linea = ";".join(map(str, data))
            archivo.write(linea + "\n")

    print("Historial guardado con éxito.")
    print("Datos exportados a Excel.")

if historial:
    historial.sort(key=lambda x: x[1])

    while True:
        busqueda = input("Queres buscar una velocidad específica?(s/n):").lower()
        if busqueda != "s":
            print("¡Hasta la próxima!")
            break
        
        try:
            objetivo = int(input("Ingresá los KMH que buscas:"))
            posicion = busqueda_binaria(historial, objetivo)

            if posicion != -1:
                res = historial[posicion]
                print(f"Encontrada! El registro de {res[1]} KMH fue el {res[0]} ({res[2]} MPH)")
            else:
                print("Esa velocidad no se encuentra en el registro")
        except ValueError:
            print("Por favor ingresá un numero entero")

# Funcion para encontrar la velocidad más alta registrada en la lista
def encontrar_record(historial):
    if not historial:
        return 0
    
    record_maximo = historial[0]

    for registro in historial:
        if registro[1] > record_maximo[1]:
            record_maximo = registro
    
    return record_maximo

record = encontrar_record(historial)
if record:
    print("--RECORD DE SESIÓN--")
    print(f"Velocidad más alta: {record[1]} km/h")
    print(f"Fecha y hora: {record[0]}")

def filtrar_velocidades_altas(historial,limite=200):
    infractores = []

    for registro in historial:
        if registro[1] > limite:
            infractores.append(registro)
    
    return infractores

lista_nueva = filtrar_velocidades_altas(historial)
print(f"Se encontraron {len(lista_nueva)} registros que superaron los 200 km/h")
for info in lista_nueva:
    print(f"El {info[0]} fuiste a {info[1]} km/h")



