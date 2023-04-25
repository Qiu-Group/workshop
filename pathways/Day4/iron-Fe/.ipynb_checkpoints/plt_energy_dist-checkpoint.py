import numpy as np
import matplotlib.pyplot as plt

np.x = [2.7, 2.8, 2.9, 3.0] # lattice paramater you changed in the calculations
np.y = [ -658.04350514, -658.05092626, -658.03076327, -657.97422666] # energy in Ry from Espresso

#plt.show()
plt.plot(np.x,np.y)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.title('Fe - Energy vs distance ')
plt.tight_layout()
plt.savefig('Energy_Fe.png', format='png', dpi=100)
