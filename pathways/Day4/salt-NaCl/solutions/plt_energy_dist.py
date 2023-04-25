import numpy as np
import matplotlib.pyplot as plt

np.x = [5.6, 5.7, 5.8, 5.9] # lattice paramater you changed in the calculations
np.y = [-755.24457736, -755.25615588, -755.24973895, -755.24096263] # energy in Ry from Espresso

#plt.show()
plt.plot(np.x,np.y)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.title('NaCl - Energy vs distance ')
plt.tight_layout()
plt.savefig('Energy_NaCl.png', format='png', dpi=100)
