import pandas as pd  

def calcular_errores(x, y, valor_real):  
    diferencia = x - y  
    error_abs = abs(valor_real - diferencia)  
    error_rel = error_abs / abs(valor_real)  
    error_pct = error_rel * 100  
    
    # Retornar resultados para almacenar en un DataFrame  
    return {  
        "Diferencia": diferencia,  
        "Error absoluto": error_abs,  
        "Error relativo": error_rel,  
        "Error porcentual": error_pct  
    }  

# datos a evaluar  
valores = [  
    (1.000001, 1.000000, 0.000001),   
    (1.000000000000001, 1.000000000000000, 0.000000000000001)  
]  

# lista para almacenar resultados  
resultados = []  

# calculae los errores para cada par de valores  
for x, y, real in valores:  
    resultado = calcular_errores(x, y, real)  
    resultados.append(resultado)  

# se crea un DataFrame con los resultados  
df = pd.DataFrame(resultados)  

# se guarda en el DataFrame en un archivo Excel  
df.to_excel("resultados_errores.xlsx", index=False)  

print("Resultados guardados en 'resultados_errores.xlsx'")