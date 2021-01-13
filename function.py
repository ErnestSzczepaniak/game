import numpy as np
import matplotlib.pyplot as plt
#

def normal_dist(points, mean, variance, scale): # x wektor warotsic , srednia, variancja
    
    indices = np.linspace(0, points, points)
    density = (1/(2*np.pi*variance**2) ) * np.exp(-0.5*((indices-mean)/variance)**2)
    m = max(density)
    for i in range(240):
        density[i] /= m
        density[i] *= scale
    
    return density


f0 = normal_dist(240, 120, 30, 0.7)
f1 = normal_dist(240, 100, 45, 0.2)
f2 = normal_dist(240, 140, 60, 0.1)



# pdf = normal_dist(240, 10, 0.5)
  
# plt.plot([index for index in range(240)],f0 , color = 'red')
# plt.plot([index for index in range(240)],f1 , color = 'green')
# plt.plot([index for index in range(240)],f2 , color = 'blue')

# plt.show()





# plt.plot(bins, ,
#          linewidth=2, color='r')
# plt.show()