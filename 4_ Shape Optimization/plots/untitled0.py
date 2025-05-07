import numpy as np
import matplotlib.pyplot as plt

nelem = [877,3488,13062,51184,139704,308277]
tpe = [1.97217832E-01,2.03080991E-01,2.05233973E-01,2.06258785E-01,2.06635843E-01,2.06822578E-01]
defo = [0.486,0.505,0.513,0.518,0.520,0.520]
stress = [89.03,117.88,194.43,303.56,414.39,525.95]

plt.plot(nelem, tpe, marker ='o')
plt.xlabel('Number of elements [-]')
plt.ylabel('TPE [J]')
plt.grid(True)
plt.show()

plt.plot(nelem,defo,marker='o')
plt.xlabel('Number of elements [-]')
plt.ylabel('Displacement [mm]')
plt.grid(True)
plt.show()

plt.plot(nelem,stress,marker='o')
plt.xlabel('Number of elements [-]')
plt.ylabel('Stress [MPa]')
plt.grid(True)
plt.show()