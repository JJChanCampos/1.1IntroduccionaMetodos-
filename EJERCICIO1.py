import numpy as np  
import pandas as pd  

epsilon = 1.0  
iteracion = 0  
resultados = []  # Lista para almacenar los resultados  

while 1.0 + epsilon != 1.0:  
    epsilon /= 2  
    iteracion += 1  
    resultados.append((iteracion, epsilon))  # Guardar iteración y epsilon  

epsilon *= 2  
resultados.append(('Final', epsilon))  # Agregar el resultado final  

# Crear un DataFrame a partir de la lista de resultados  
df = pd.DataFrame(resultados, columns=['Iteración', 'Precisión de máquina'])  

# Guardar el DataFrame en un archivo Excel  
df.to_excel('precision_maquina.xlsx', index=False)  

print("Los resultados se han guardado en 'precision_maquina.xlsx'")