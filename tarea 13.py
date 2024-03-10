def convertir_fahrenheit_a_celsius(fahrenheit):
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    Args:
    - fahrenheit (float): Temperatura en grados Fahrenheit.


    Returns:
    - float: Temperatura convertida a grados Celsius.
    """
    return (fahrenheit - 32) * 5/9

def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio para datos de múltiples ciudades y semanas, convirtiendo de Fahrenheit a Celsius.

    Args:
    - datos_temperatura (dict): Un diccionario donde las claves son los nombres de las ciudades y los valores son listas
      de listas que representan las temperaturas diarias en grados Fahrenheit para cada semana.

    Returns:
    - dict: Un diccionario que contiene el nombre de la ciudad como clave y la temperatura promedio en grados Celsius como valor.
    """
    if not datos_temperatura:
        print("Error: No se proporcionaron datos de temperatura.")
        return

    temperatura_promedio_ciudad = {}

    for ciudad, temperaturas_semana in datos_temperatura.items():
        temperatura_promedio_semana = []

        for semana in temperaturas_semana:
            temperatura_celsius_semana = [convertir_fahrenheit_a_celsius(temp) for temp in semana]
            temperatura_promedio_semana.append(sum(temperatura_celsius_semana) / len(temperatura_celsius_semana))

        temperatura_promedio_ciudad[ciudad] = sum(temperatura_promedio_semana) / len(temperatura_promedio_semana)

    return temperatura_promedio_ciudad

# Ejemplo de uso:
datos_temperatura = {
    'CiudadA': [[77, 78, 75, 72, 71, 68, 69], [72, 75, 77, 73, 68, 66, 64]],
    'CiudadB': [[86, 89, 84, 82, 80, 79, 77], [82, 80, 79, 86, 89, 88, 84]],
    'CiudadC': [[64, 68, 67, 72, 70, 73, 75], [77, 80, 81, 75, 73, 72, 68]]
}


# Imprimir el código
print("def convertir_fahrenheit_a_celsius(fahrenheit):")
print('    return (fahrenheit - 32) * 5/9')
print()
print("def calcular_temperatura_promedio(datos_temperatura):")
print('    if not datos_temperatura:')
print('        print("Error: No se proporcionaron datos de temperatura.")')
print('        return')
print()
print('    temperatura_promedio_ciudad = {}')
print()
print('    for ciudad, temperaturas_semana in datos_temperatura.items():')
print('        temperatura_promedio_semana = []')
print()
print('        for semana in temperaturas_semana:')
print('            temperatura_celsius_semana = [convertir_fahrenheit_a_celsius(temp) for temp in semana]')
print('            temperatura_promedio_semana.append(sum(temperatura_celsius_semana) / len(temperatura_celsius_semana))')
print()
print('        temperatura_promedio_ciudad[ciudad] = sum(temperatura_promedio_semana) / len(temperatura_promedio_semana)')
print()
print('    return temperatura_promedio_ciudad')
print()
print(f'# Ejemplo de uso:')
print(f'datos_temperatura = {datos_temperatura}')
print(f'resultado = calcular_temperatura_promedio(datos_temperatura)')
print()
print('for ciudad, temperatura_promedio in resultado.items():')
print('    print(f"Temperatura promedio en {ciudad}: {temperatura_promedio:.2f}°C")')
