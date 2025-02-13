#Modificado por: Jose Chan

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #en este caso, al elaborarlo en collab tuve la idea que de una vez me mande el archivo excel, para ello importamos la libreria de pandas

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []

# Calculo los errores de la problematica
for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}")

# Se guardan los resultados en el data frame perteneciente de pandas
df = pd.DataFrame({
    'N': N_values,
    'Error Absoluto': errors_abs,
    'Error Relativo': errors_rel
})

# los errores se guardan y mandan a otro DataFrame para convertirlo en un archivo Excel
df.to_excel('errores_pi.xlsx', index=False)

# metodo para elaborar las graficas correspondientes .
plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de pi')
plt.show()