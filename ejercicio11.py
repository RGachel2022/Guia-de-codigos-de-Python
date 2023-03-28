def calcular_factura_agua(consumo_agua):
    cuota_fija = 6  
    tarifa_adicional = 0  
    
    if consumo_agua <= 18:
        tarifa_adicional = 0
    
    elif consumo_agua > 18 and consumo_agua <= 28:
        tarifa_adicional = 0.45 * (consumo_agua - 18)

    elif consumo_agua > 28:
        tarifa_adicional = 0.45 * (28 - 18) + 0.65 * (consumo_agua - 28)
    
    total_factura = cuota_fija + tarifa_adicional
    
    return total_factura

consumo_cliente = float(input("Ingrese el numero de consumo de agua en metros cúbicos: "))

factura_cliente = calcular_factura_agua(consumo_cliente)

print(f"El consumo de agua del cliente es: {consumo_cliente} m^3")
print(f"Facturación: ${factura_cliente:.2f}")
