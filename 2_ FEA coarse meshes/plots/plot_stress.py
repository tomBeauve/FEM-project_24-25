import numpy as np
import matplotlib.pyplot as plt

T3_nelem = [1736,6812,26877,106484,293558,661725]
T6_nelem = [1736,6812,26877,106484,293558,661725]
Q6_nelem = [874,3451,13170,51573,140646,312350]
Q8_nelem = [874,3451,13170,51573,140646,312350]

T3_zone1 = [239.37,363.39,396.51,417.47,439.58,451.45]
T6_zone1 = [217.15,319.66,353.22,381.90,409.72,423.43]
Q6_zone1 = [202.62,254.37,326.63,371.03,408.73,420.16]
Q8_zone1 = [201.95,248.36,322.94,369.55,402.57,416.33]

T3_zone2 = [186.81,305.40,315.97,318.93,340.58,347.22]
T6_zone2 = [172.36,275.28,270.56,289.41,316.97,325.56]
Q6_zone2 = [137.44,193.42,264.42,268.06,330.96,323.17]
Q8_zone2 = [135.92,184.22,257.23,262.63,308.82,320.33]

T3_zone3 = [139.73,226.53,231.88,230.38,254.86,256.12]
T6_zone3 = [132.76,201.11,203.28,215.02,236.92,240.98]
Q6_zone3 = [112.01,151.70,203.43,207.56,226.47,225.59]
Q8_zone3 = [110.51,146.57,196.94,202.60,222.94,225.06]

T3_zone4 = [123.22,158.16,194.86,199.54,206.59,218.41]
T6_zone4 = [129.10,141.15,172.76,182.17,192.05,204.71]
Q6_zone4 = [86.84,146.77,156.07,173.16,190.54,203.34]
Q8_zone4 = [85.09,137.68,151.85,167.63,185.77,200.86]

T3_zone5 = [62.28,100.12,166.70,259.45,352.82,448.01]
T6_zone5 = [52.81,79.56,130.04,201.75,275.07,350.20]
Q6_zone5 = [39.99,70.17,114.12,179.40,245.38,313.25]
Q8_zone5 = [35.81,60.18,97.63,153.78,210.94,270.03]

T3_zone6 = [49.81,65.55,110.66,173.64,237.02,301.23]
T6_zone6 = [40.33,53.83,86.04,131.35,180.39,231.05]
Q6_zone6 = [41.63,45.99,73.40,116.56,160.75,207.36]
Q8_zone6 = [39.51,47.32,69.44,101.09,136.11,176.64]


plt.plot(T3_nelem, T3_zone1, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone1, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone1, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone1 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.legend()
plt.title('Stress in zone 1')
plt.grid(True)
plt.show()

plt.plot(T3_nelem, T3_zone2, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone2, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone2, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone2 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.title('Stress in zone 2')
plt.legend()
plt.grid(True)
plt.show()


plt.plot(T3_nelem, T3_zone3, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone3, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone3, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone3 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.title('Stress in zone 3')
plt.legend()
plt.grid(True)
plt.show()


plt.plot(T3_nelem, T3_zone4, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone4, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone4, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone4 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.title('Stress in zone 4')
plt.legend()
plt.grid(True)
plt.show()


plt.plot(T3_nelem, T3_zone5, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone5, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone5, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone5 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.title('Stress in zone 5')
plt.legend()
plt.grid(True)
plt.show()


plt.plot(T3_nelem, T3_zone6, marker='o', label='T3')
plt.plot(T6_nelem, T6_zone6, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_zone6, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_zone6 , marker='o', label='Q8')

plt.xlabel('Number of elements ')
plt.ylabel('Stress ')
plt.title('Stress in zone 6')
plt.legend()
plt.grid(True)
plt.show()
