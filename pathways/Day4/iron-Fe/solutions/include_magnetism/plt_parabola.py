import numpy as np
import matplotlib.pyplot as plt

np.x = [2.7, 2.8, 2.9, 3] # lattice paramater you changed in the calculations

#np.y contains non-magnetic results from earlier
#np.y = [ -658.04350514, -658.05092626, -658.03076327, -657.97422666] # energy in Ry from Espresso
np.y_magnetic = [-658.09493388, -658.11811277, -658.11135877, -658.08833277]   

coeff = np.polyfit(np.x, np.y_magnetic, 2)  # coeff contains a, b and c from quadratic fit of ax^2 + bx + c

np.x2 = np.linspace(2.5, 3.2, num=10) # generate 10 points between 3.8 and 4.5
np.quad_fit = [coeff[0]*elem**2 + coeff[1]*elem + coeff[2] for elem in np.x2] 

#plt.show()
plt.plot(np.x2, np.quad_fit)
plt.xlabel('Lattice constant in $\AA$')
plt.ylabel('Energy in Ry')
plt.tight_layout()
plt.savefig('Energy_prbla_Fe.png', format='png', dpi=100)



# to convert from Ry to eV we need to muliply the energies by 13.61 since 1 Ry = 13.61 eV

for i in range(len(np.y_magnetic)):
    np.y_magnetic[i] = np.y_magnetic[i]*13.61

print('Energies in eV', np.y_magnetic)
