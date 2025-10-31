import csv
from datetime import datetime
import os
import json
#####Paso 1: Leer el archivo csv

nombre_archivo = 'actividad 2.csv'
# Esta lista guardará todos los datos como diccionarios
entrenamientos = [] 
try:
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
#DictReader: lee la primera línea como encabezados (claves del diccionario)
        lector = csv.DictReader(archivo)
# Recorremos cada fila y la añadimos a la lista entrenamientos
        for fila_diccionario in lector:
            entrenamientos.append(fila_diccionario)
    print(f" Paso 1: Archivo '{nombre_archivo}' leído. Se cargaron {len(entrenamientos)} registros.")
except FileNotFoundError:
    print(f" error: No se encontró el archivo '{nombre_archivo}'.")
    print("asegúrate de que el archivo esté en la misma carpeta que este script.")
except Exception as e:
    print(f" ocurrió un error inesperado durante la lectura: {e}")
print (entrenamientos)
# Definimos nombres de días (weekday() devuelve 0=Lunes, 6=Domingo)
dia_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
####Paso 2:Identificar el día de la semana de cada entrenamiento.

entrenamientos_procesados = []
for registro in entrenamientos:
    timestamp_str = registro['timestamp'] 
#Convertir la cadena de texto a un objeto datetime
    fecha_dt = datetime.strptime(timestamp_str, '%m/%d/%Y %H:%M')
#Obtener el número del día de la semana (0=Lunes, 6=Domingo)
    indice_dia = fecha_dt.weekday()
#Asignar el nombre del día al registro
    registro['dia_nombre'] = dia_semana[indice_dia]
    entrenamientos_procesados.append(registro)
print(" Paso 2: Día de la semana añadido a todos los registros.")
#####Paso 3:Indicar cuál es el/los dia/s de la semana que tienen más sesiones de entrenamiento

#Contar las sesioness de cada día usando un diccionario
conteo_dias_manualmente = {}
for registro in entrenamientos_procesados:
    dia = registro['dia_nombre']
#Si el día ya está en el diccionario, le sumamos 1 a su cuenta
    if dia in conteo_dias_manualmente:
        conteo_dias_manualmente[dia] += 1
#Si es la primera vez que vemos ese día, lo inicializamos en 1
    else:
        conteo_dias_manualmente[dia] = 1
#Encontrar el dia que tuvo mas sesiones de entrenamientos
max_sesiones = 0
if conteo_dias_manualmente:
# Buscamos el valor máximo entre todos los conteos guardados
    max_sesiones = max(conteo_dias_manualmente.values())
#Identificar todos los días que igualan ese máximo
dias_maximos = []
for dia, cantidad in conteo_dias_manualmente.items():
    if cantidad == max_sesiones:
        dias_maximos.append(dia)
print(f"Paso 3: el/Los día/s con más sesiones ({max_sesiones} sesiones) es/son:")
print(dias_maximos)
####Paso 4: Cuantos dias pasaron entre el primer y el ultimo entrenamiento

fechas_dt = []
#Recorremos la lista para extraer y convertir solo la fecha
for registro in entrenamientos_procesados:
    timestamp_str = registro['timestamp']
# Convertimos el texto a objeto datetime
    fecha_dt_completa = datetime.strptime(timestamp_str, '%m/%d/%Y %H:%M')    
# Nos quedamos solo con la parte de la fecha (día, mes, año)
    fecha_sola = fecha_dt_completa.date() 
    fechas_dt.append(fecha_sola)
#Calcular el rango
dias_transcurridos = 0
if fechas_dt:
# Encontramos la fecha más antigua y la más reciente en la lista de fechas
    fecha_inicio = min(fechas_dt)
    fecha_fin = max(fechas_dt)
#Calculamos la diferencia en días
    diferencia = fecha_fin - fecha_inicio
    dias_transcurridos = diferencia.days #.days se usa para contar el dia completo
    print("Paso 4: RESULTADOS")
    print(f"Primera sesión: {fecha_inicio}")
    print(f"Última sesión: {fecha_fin}")
    print(f"Días transcurridos: {dias_transcurridos} días.")

else:
#Este else se ejecuta si la lista fechas_dt estaba vacia
    print("No hay datos de entrenamiento para calcular el rango.")
####Paso 5: mostrar el campeon que mas entreno

#Contar las ocurrencias de cada campeón usando un diccionario normal
conteo_campeones = {}
for registro in entrenamientos_procesados:
#Extraemos el nombre del campeón
    campeon = registro['campeon']
# Lógica manual de conteo: Si ya existe, suma; si no, inicializa en 1
    if campeon in conteo_campeones:
        conteo_campeones[campeon] += 1
    else:
        conteo_campeones[campeon] = 1
#Encontrar el número máximo de sesiones
max_entrenos = 0
if conteo_campeones:
#función max() sobre los valores(la cantidad seria) del diccionario
    max_entrenos = max(conteo_campeones.values())
#Identificar todos los campeones que igualan ese máximo por las dudas que haya algun empate
campeones_maximos = []
for campeon, cantidad in conteo_campeones.items():
    if cantidad == max_entrenos:
        campeones_maximos.append(campeon)
#Mostrar el resultado del paso 5
print("Paso 5: Campeón que más entreno")
print(f"El campeón que más entrenó ({max_entrenos} sesiones) es/son:")
print(f"{campeones_maximos}")
####Paso 6: Promedio de entrenamientos por cada día de la semana

print(" Paso 6: Conteo de entrenamientos por dia de la semana")
for dia in dia_semana:
# Usamos .get() para buscar el día en el diccionario de conteo.
    cantidad = conteo_dias_manualmente.get(dia, 0) #(si el dia no existe o no hubo entrenamiento ese dia devulve 0)
    print(f"{dia}: {cantidad} sesiones")
####Paso 7:  Campeón que más entrena los fines de semana (sábado y domingo)

fines_de_semana = ["Sábado", "Domingo"]
conteo_finde = {}
campeon_mas_entrenado_finde = None
max_entrenos_finde = 0
for registro in entrenamientos_procesados:
    dia = registro['dia_nombre']
#Verificamos si el día es Sábado O Domingo
    if dia in fines_de_semana:
        campeon = registro['campeon']
# Contamos solo si es fin de semana
        if campeon in conteo_finde:
            conteo_finde[campeon] += 1
        else:
            conteo_finde[campeon] = 1
#Encontrar el máximo y el campeón
if conteo_finde:
# Encontrar la cantidad máxima
    max_entrenos_finde = max(conteo_finde.values())
# Encontrar el campeón asociado a esa cantidad
    for campeon, cantidad in conteo_finde.items():
        if cantidad == max_entrenos_finde:
            campeon_mas_entrenado_finde = campeon
# Rompemos el bucle en cuanto encontramos el primero, ya que solo pide 'el' campeón.
            break 
#Resultado paso 7:
if max_entrenos_finde > 0:
    print(f"paso 7: El campeón que más entrena los fines de semana ({max_entrenos_finde} sesiones) es:")
    print(f"{campeon_mas_entrenado_finde}")
else:
    print("No se registraron entrenamientos durante el fin de semana (Sábado o Domingo).")
###Paso 8: En una carpeta llamada salida, que se debe generar, crear un archivo .csv que para
#cada campeón muestre la cantidad de entrenamientos (indicar campeón y cantidad)

carpeta_salida = 'salida'
ruta_csv_final = os.path.join(carpeta_salida, "campeones_entrenamientos.csv")
#Crear la carpeta salida si no existe
try:
    if not os.path.exists(carpeta_salida):
        os.mkdir(carpeta_salida)
        print(f" Carpeta '{carpeta_salida}' creada.")
except OSError as e:
    print(f" Error al crear la carpeta '{carpeta_salida}': {e}")
#Escribir el archivo CSV
if conteo_campeones: # Solo escribimos si hay datos de conteo
# Abrimos el archivo en modo 'w' (escritura)
    with open(ruta_csv_final, mode='w', newline='', encoding='utf-8') as archivo_salida:
        # csv.writer es para escribir filas simples (no diccionarios)
        escritor = csv.writer(archivo_salida)
# Escribir el encabezado (los nombres de las columnas)
        escritor.writerow(['campeon', 'cantidad'])
# Escribir los datos: recorremos el diccionario y escribimos cada par (campeón, cantidad)
        for campeon, cantidad in conteo_campeones.items():
            escritor.writerow([campeon, cantidad])
    print(f" Archivo CSV de conteo generado en: {ruta_csv_final}")
else:
    print(" No se generó el CSV porque no hay datos de campeones para contar.")
print(f"Paso 8: La cantidad de entrenamientos por campeon: es {conteo_campeones}")
###Paso 9: Generar un archivo .json en la misma carpeta (salida) que indique el total de
#registros y para cada día, los campeones que entrenaron, junto con cuántas veces
#entrenó cada uno.
carpeta_salida = 'salida'
ruta_json_final = os.path.join(carpeta_salida, "resumen_diario_manual.json")
#Crear la estructura principal del JSON
resumen_json = {
    "total_registros": len(entrenamientos_procesados),
    "dias": {}  # guardamos el detalle de cada día
}


for dia_nombre in dia_semana:
    #Este diccionario va a guardar el conteo de campeones solo para este día
    conteo_campeones_dia = {} 

    for registro in entrenamientos_procesados:
#Revisamos solo los registros del día actual
        if registro['dia_nombre'] == dia_nombre:
            campeon = registro['campeon']
#Sumamos 1 al campeón de este día
            if campeon in conteo_campeones_dia:
                conteo_campeones_dia[campeon] += 1
            else:
                conteo_campeones_dia[campeon] = 1 # Inicializamos en 1
#Guardar en la estructura JSON
    if conteo_campeones_dia:
        resumen_json['dias'][dia_nombre] = conteo_campeones_dia
       
#Escribir el archivo JSON
if entrenamientos_procesados:
    with open(ruta_json_final, mode='w', encoding='utf-8') as archivo_salida:
        print(f" Archivo JSON de resumen  generado en: {ruta_json_final}") 
print(f"Paso 9: {resumen_json}") 