def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    impuesto = 21
    print(precio_base* impuesto/100)
    print(precio_base+impuesto)
    print((precio_base+impuesto)*10/100)
    print((precio_base+impuesto) + (precio_base+impuesto)*10/100)
