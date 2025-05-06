import numpy as np
import matplotlib.pyplot as plt

T3_area = [2.953108e3, 2.953056e3, 2.952994e3, 2.952984e3, 2.952980e3, 2.952310e3]
T6_area = [2.952980e3, 2.952978e3, 2.952978e3, 2.952978e3, 2.952978e3, 2.952309e3]
Q6_area = [2.953285e3, 2.953056e3, 2.953002e3, 2.952984e3, 2.952980e3, 2.952310e3]
Q8_area = [2.952980e3, 2.952978e3, 2.952978e3, 2.952978e3, 2.952978e3, 2.952309e3]

T3_time = [15, 15, 24, 51, 133, 278]
T6_time = [16, 17, 37, 168, 493, 545]
Q6_time = [14, 15, 20, 49, 84, 195]
Q8_time = [14, 12, 18, 44, 106, 354]

T3_tpe = [1.077717, 1.165658, 1.200782, 1.213489, 1.217456, 1.217701]
T6_tpe = [1.205077, 1.213902, 1.218439, 1.220382, 1.221086, 1.219894]
Q6_tpe = [1.164085, 1.199438, 1.212475, 1.217747, 1.219706, 1.219087]
Q8_tpe = [1.202412, 1.212688, 1.217913, 1.220066, 1.220980, 1.219870]

T3_ndof = [2138, 7820, 29042, 113002, 309266, 692728]
T6_ndof = [7990, 29664, 113560, 446844, 1228438, 2757962]
Q6_ndof = [5654, 20796, 79172, 314012, 850144, 1874352]
Q8_ndof = [5990, 21456, 80484, 316612, 854472, 1880842]

T3_nelem = [1817, 7167, 27736, 110418, 304951, 686251]
T6_nelem = [1837, 7090, 27736, 110418, 304951, 686251]
Q6_nelem = [891, 3358, 12984, 51908, 140974, 311315]
Q8_nelem = [891, 3358, 12984, 51908, 140974, 311315]

#area
plt.plot(T3_nelem, T3_area, marker='o', label='T3')
plt.plot(T6_nelem, T6_area, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_area, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_area , marker='o', label='Q8')
plt.axhline(2.9526e3 , label='Reference')


plt.xlabel('Number of elements ')
plt.ylabel('Area ')
plt.title('Approximate area')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(T3_ndof, T3_area, marker='o', label='T3')
plt.plot(T6_ndof, T6_area, marker='o', label='T6')
plt.plot(Q6_ndof, Q6_area, marker='o', label='Q6')
plt.plot(Q8_ndof, Q8_area , marker='o', label='Q8')
plt.axhline(2.9526e3 , label='Reference')


plt.xlabel('Number of degrees of freedom ')
plt.ylabel('Area ')
plt.title('Approximate area')
plt.legend()
plt.grid(True)
plt.show()

#time
plt.plot(T3_ndof, T3_time, marker='o', label='T3')
plt.plot(T6_ndof, T6_time, marker='o', label='T6')
plt.plot(Q6_ndof, Q6_time, marker='o', label='Q6')
plt.plot(Q8_ndof, Q8_time , marker='o', label='Q8')


plt.xlabel('Number of degrees of freedom ')
plt.ylabel('Time')
plt.title('Computation time')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(T3_nelem, T3_time, marker='o', label='T3')
plt.plot(T6_nelem, T6_time, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_time, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_time , marker='o', label='Q8')


plt.xlabel('Number of elements ')
plt.ylabel('Time  ')
plt.title('Computation time')
plt.legend()
plt.grid(True)
plt.show()
#tpe
plt.plot(T3_ndof, T3_tpe, marker='o', label='T3')
plt.plot(T6_ndof, T6_tpe, marker='o', label='T6')
plt.plot(Q6_ndof, Q6_tpe, marker='o', label='Q6')
plt.plot(Q8_ndof, Q8_tpe , marker='o', label='Q8')


plt.xlabel('Number of degrees of freedom ')
plt.ylabel('TPE')
plt.title('TPE')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(T3_nelem, T3_tpe, marker='o', label='T3')
plt.plot(T6_nelem, T6_tpe, marker='o', label='T6')
plt.plot(Q6_nelem, Q6_tpe, marker='o', label='Q6')
plt.plot(Q8_nelem, Q8_tpe, marker='o', label='Q8')


plt.xlabel('Number of elements ')
plt.ylabel('TPE  ')
plt.title('TPE')
plt.legend()
plt.grid(True)
plt.show()
