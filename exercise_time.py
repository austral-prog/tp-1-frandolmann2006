def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    hora_completa = 3600
    minutos= 60
    print(total_segundos//60//60)
    print((total_segundos//hora_completa)%minutos)
    print(total_segundos-hora_completa-minutos)
