import numpy as np 
import skfuzzy as sk
import matplotlib.pyplot as plt 

x = np.arange(-11, 11, 1)

vd_gaussiana = sk.gaussmf(x, 0, 1)

plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')
plt.title('Calidad del servicio en un Restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)