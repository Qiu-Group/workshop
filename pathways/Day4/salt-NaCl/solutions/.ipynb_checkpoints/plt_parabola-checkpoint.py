import numpy as np
import matplotlib.pyplot as plt

np.x = [5.6, 5.7, 5.8, 5.9] # lattice paramater you changed in the calculations
np.y = [-755.24457736, -755.25615588, -755.24973895, -755.24096263] # energy in Ry from Espresso

coeff = np.polyfit(np.x, np.y, 2)  # coeff contains a, b and c from quadratic fit of ax^2 + bx + c

np.x2 = np.linspace(5.4, 6.1, num=10) # generate 10 points between 3.8 and 4.5
np.quad_fit = [coeff[0]*elem**2 + coeff[1]*elem + coeff[2] for elem in np.x2] 

#plt.show()
plt.plot(np.x2, np.quad_fit)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.title('NaCl - Energy vs distance quad. fit')
plt.tight_layout()
plt.savefig('Energy_prbla_NaCl.png', format='png', dpi=100)



# to convert from Ry to eV we need to muliply the energies by 13.61 since 1 Ry = 13.61 eV

for i in range(len(np.y)):
    np.y[i] = np.y[i]*13.61

print('Energies in eV', np.y)
