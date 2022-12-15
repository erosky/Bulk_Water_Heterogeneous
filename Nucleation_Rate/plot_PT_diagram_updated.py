import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Lines of constant J=10^27

pressures=[-100, -50, 1]
pmin = -120.0
pmax = 100.0
P_range=np.arange(pmin, pmax, 5)


mW_J=[209, 207.75, 205.5]
mW_dJ=[-64, -65.25, -67.5]
mW_dJ_th=[-65.3, -66.4, -67.5]
mW_melt=[275, 274, 273]
mW_dmelt=[2, 1, 0]

MLmW_J=[223.4, 219.6, 214.5]
MLmW_dJ=[-68.6, -72.4, -77.5]
MLmW_dJ_th=[-70.7, -74.1, -77.5]
MLmW_melt=[298, 295, 292]
MLmW_dmelt=[6, 3, 0]

MLmW_Jhigh=[-64, -68, -72]
MLmW_Jlow=[-75, -76, -80]


# Heterogeneous Freezing lines of J=10^24

#mW_het=[220.8575, 219.4, 218.4] # old data
#mW_het_th=[-52.25, -53.75, -54.75]
#mW_dJ_het=[-51.895, -52.995, -54.095]



mW_het=[219.6, 217.87, 216.8]
mW_dJ_het=[]
for t in mW_het:
	mW_dJ_het.append(t-273)

# theoretical approximation with dT of 3.4
mW_het_th=[mW_dJ_het[2]+2, mW_dJ_het[2]+1, mW_dJ_het[2]]

	
	
# Heterogeneous error bounds
mW_het_dT = [2.49, 3.13, 3.2]
mW_het_Jhigh=[]
mW_het_Jlow=[]
for i,t in enumerate(mW_dJ_het):
	mW_het_Jhigh.append(t + mW_het_dT[i]/2)
	mW_het_Jlow.append(t - mW_het_dT[i]/2)





#--------------------
# Marcolli
#-------------------

def Mar_T(P):
	T = 557.2-273*np.exp((300.0+P)**2/2270000.0)
	return T



plt.title('Melting Point, Homogeneous Freezing, and Heterogeneous Freezing Curves')
plt.xlabel('Pressure (MPa)')
plt.ylabel(r'Degrees K from 0 MPa $T_{melt}$')


plt.hlines(0, pmin, pmax, colors=['k'])
plt.text(-115, -3, r'$T_{melt}$ at 0 MPa')

plt.plot(P_range, Mar_T(P_range)-273, '#707070', label=r'$T_{melt}$ Marcolli')
#plt.plot(P_range, Mar_T(P_range+307)-273, '#adadad', label=r'$J=10^8$ Marcolli')


'''
plt.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'MLmW $T_{melt}$')
plt.plot(pressures, MLmW_dJ, '^g', linewidth=1.0, label=r'MLmW $J=10^{32} m^{-3}s^{-1}$')
'''

plt.plot(pressures, mW_dmelt,'bo', linewidth=1.0, label=r'mW $T_{melt}$')
plt.plot(pressures, mW_dJ,'^b', linewidth=1.0, label=r'mW $J=10^{32} m^{-3}s^{-1}$')


plt.xlim(pmin, pmax)
plt.legend(loc='lower right')
plt.grid(color='#d4d4d4', linestyle='--', linewidth=1)

plt.tight_layout()
plt.savefig('plot_PT_delta_mW.png', dpi=300)


#--------------------
# Break y-axis

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

# plot melting data on both axis
ax.hlines(0, pmin, pmax, colors=['k'])
ax.text(-115, -3, r'$T_{melt}$ at 0 MPa')

ax.plot(P_range, Mar_T(P_range)-273, '#707070')
ax.plot(pressures, mW_dmelt,'go', fillstyle='none', linewidth=1.0)
#ax.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'MLmW $T_{melt}$')


# plot all data on second axis
#--- melting data
ax2.plot(P_range, Mar_T(P_range)-273, '#707070', label=r'$T_{melt}$ (Marcolli 2017)')
ax2.plot(pressures, mW_dmelt,'go', fillstyle='none', linewidth=1.0, label=r'$T_{melt}$ (Rosky 2022)')
#ax2.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'ML-mW $T_{melt}$')

#--- freezing data

ax2.plot(pressures, mW_dJ_th,'b--', linewidth=1.5)
ax2.plot(pressures, mW_dJ,'bo', fillstyle='none', linewidth=1.0, label=r'$J_{hom}=10^{32}$ m$^{-3}$s$^{-1}$ (Rosky 2022)')
ax2.fill_between(pressures, mW_het_Jhigh, mW_het_Jlow, color='r', alpha=0.2)
ax2.plot(pressures, mW_dJ_het, 'ro', linewidth=1.0, label=r'$J_{het}=10^{24}$ m$^{-2}$s$^{-1}$')
ax2.plot(pressures, mW_het_th,'r--', linewidth=1.5, label='Equation 1')




'''
ax2.fill_between(pressures, MLmW_Jhigh, MLmW_Jlow, color='g', alpha=0.2)
ax2.plot(pressures, MLmW_dJ, '^g', linewidth=1.0, label=r'ML-mW $J=10^{32}$ m$^{-3}$s$^{-1}$')
ax2.plot(pressures, MLmW_dJ_th, 'g--', linewidth=1.5, label='Equation 1')
'''






# zoom-in / limit the view to different portions of the data
ax.set_ylim(-5., 10.)  # melting 
ax2.set_ylim(-75., -50.)  # homogeneous freezing

ax.set_xlim(pmin, pmax+20)
ax2.set_xlim(pmin, pmax+20)
ax2.legend(loc='lower right', fontsize='small')

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

ax.grid(color='#d4d4d4', linestyle='--', linewidth=1)
ax2.grid(color='#d4d4d4', linestyle='--', linewidth=1)

# This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'

ax.set_title('Homogeneous and heterogeneous nucleation rate, mW')
ax2.set_xlabel('Pressure (MPa)')
ax2.set_ylabel(r'T - T$_{melt}$')
plt.savefig('PT_diagram_mW_bounds.png', dpi=300)


