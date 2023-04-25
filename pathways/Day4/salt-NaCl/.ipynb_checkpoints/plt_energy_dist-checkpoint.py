import numpy as np
import matplotlib.pyplot as plt

np.x = [5.3, 5.4, 5.5, 5.6] # lattice paramater you changed in the calculations
np.y = [ ??, ??, ??, ??] # energy in Ry from Espresso

#plt.show()
plt.plot(np.x,np.y)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.title('NaCl - Energy vs distance ')
plt.tight_layout()
plt.savefig('Energy_NaCl.png', format='png', dpi=100)
