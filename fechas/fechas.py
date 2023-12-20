import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()

# Solicitar fecha de nacimiento al usuario
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")

# Convertir la cadena de fecha en un objeto de fecha
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

# Calcular la edad en años
edad = fecha_actual.year - fecha_nacimiento.year

# Imprimir la edad calculada
print("Tu edad es:", edad, "años")

# Calcular los segundos faltantes para el próximo cumpleaños
fecha_cumpleanos = datetime.datetime(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day)

if fecha_actual > fecha_cumpleanos:
    fecha_cumpleanos = datetime.datetime(fecha_actual.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

diferencia = fecha_cumpleanos - fecha_actual
segundos_faltantes = diferencia.total_seconds()

# Imprimir los segundos faltantes para el cumpleaños
print("Faltan", int(segundos_faltantes), "segundos para tu próximo cumpleaños")
