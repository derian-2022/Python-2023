from datetime import date

# puede llamar a la // función today():

# print(date.today()) # Forma Correcta = 2023-08-30


# Conversión de tipos de datos Quiere usar una fecha con algo, normalmente una cadena. Si, por ejemplo, desea mostrar la fecha de hoy en la consola, podría experimentar algún problema:

# print("Today's date is: " + date.today()) # ERROR

print("Today's date is: " + str(date.today())) # La Mejor forma = Today's date is: 2023-08-30


