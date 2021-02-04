#se escriben con [] o list
def promedio_temps(registro):
    sumatoria = 0
    for temp in registro:
        sumatoria += float(temp) #se convierte a float para un valor más 'exacto'

    promedio = sumatoria/len(registro)

    return promedio

if __name__ == '__main__':
    registro_temps = [35, 33, 38, 36, 35, 34, 35, 35]

    avrg_promedio = promedio_temps(registro_temps)

    print('El promedio de las temperaturas fue de {} °C'.format(avrg_promedio))
