import numpy as np
import matplotlib.pyplot as plt

np.x = [4, 4.1, 4.2, 4.3] # lattice paramater you changed in the calculations
np.y = [ -3100.51190282, -3100.54572391, -3100.54879324, -3100.53026913] # energy in Ry from Espresso

#plt.show()
plt.plot(np.x,np.y)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.savefig('Energy.png', format='png', dpi=100)
