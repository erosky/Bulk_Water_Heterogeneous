import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




#Data
unconfined = [[1,-500,-1000],[227.8, 236, 241],[4/2, 5.9/2, 8/2]]
sixlayer = [[1, -500, -1000],[234, 244, 250.56],[3.7/2, 3.3/2, 5.27/2]]
eightlayer = [[1, -500, -1000],[226.6, 235.5, 241],[3.9/2, 5.27/2, 3.0724/2]]
tenlayer = [[1, -500, -1000], [227.6, 235.4, 240.46], [3.6/2, 2.6275/2, 2.32/2]]



# best fit of data
def linear(x,a,b):
	return a*x+b

popt_un, pcov_un = curve_fit(linear, unconfined[0], unconfined[1], sigma=unconfined[2])
popt_8, pcov_8 = curve_fit(linear, eightlayer[0], eightlayer[1], sigma=eightlayer[2])


un_fit = []
for p in [1,-500]:
	un_fit.append(popt_un[0]*p+popt_un[1])
	
eight_fit = []
for p in [1,-500]:
	eight_fit.append(popt_8[0]*p+popt_8[1])





a = plt.subplot(111)

#plt.plot([1,-500], un_fit, 'k--') 
#plt.plot([1,-500], eight_fit, 'b--') 
plt.errorbar(unconfined[0], unconfined[1], yerr=unconfined[2], fmt='ko', alpha=0.8, capsize=5.0, label=r'Unconfined')
plt.errorbar(tenlayer[0], tenlayer[1], yerr=tenlayer[2], fmt='gs', alpha=0.8,linewidth=1.0, capsize=5.0, label=r'30$\AA$')
plt.errorbar(eightlayer[0], eightlayer[1], yerr=eightlayer[2], fmt='bs', alpha=0.5, linewidth=1.0, capsize=5.0, label=r'24$\AA$')
plt.errorbar(sixlayer[0], sixlayer[1], yerr=sixlayer[2], fmt='rs', alpha=0.8, linewidth=1.0, capsize=5.0, label=r'18$\AA$')




#plt.xlim(0, 0.2)
plt.ylim(223, 258)
plt.xlabel(r'Pressure (atm)')
plt.ylabel(r'Temperature (K) of $j_{het}=10^{24}$ s$^{-1}$m$^{-2}$')

#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 1.05), ncol=1, fancybox=True, shadow=True)
plt.grid(color='#d4d4d4', linestyle='--', linewidth=1)
#plt.legend(loc='lower left', ncol=1, fancybox=True, shadow=True)
plt.legend(loc='upper center', mode = "expand", ncol = 4)

plt.savefig('confinement_legend.png', dpi=1000)



