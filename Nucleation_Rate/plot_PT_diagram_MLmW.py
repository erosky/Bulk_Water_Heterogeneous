import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Lines of constant J=10^27

pressures=[-100, -50, 1]
pmin = -120.0
pmax = 20.0
P_range=np.arange(pmin, pmax, 5)


MLmW_J=[223.4, 219.6, 214.5]
MLmW_dJ=[-68.6, -72.4, -77.5]
MLmW_dJ_th=[-70.7, -74.1, -77.5]
MLmW_melt=[298, 295, 292]
MLmW_dmelt=[6, 3, 0]

MLmW_Jhigh=[-64, -68, -72]
MLmW_Jlow=[-75, -76, -80]

MLmW_dT=[]
for i,t in enumerate(MLmW_Jhigh):
	MLmW_dT.append(t - MLmW_Jlow[i])


# best fit of homogeneous data
# a1, b1 = np.polyfit([-100, -50, 1], MLmW_dJ, 1)


# Heterogeneous Freezing lines of J=10^24

#MLmW_het=[239.34, 234.5, 227.8]
MLmW_het=[241, 236, 227.8]
#MLmW_het=[241, 236, 230]
MLmW_dJ_het=[]
for t in MLmW_het:
	MLmW_dJ_het.append(t-292)



# Heterogeneous error bounds

#MLmW_het_dT = [8, 5.9, 5.6]
#MLmW_het_dT = [2.8, 3.0, 4.0]
MLmW_het_dT = [8/2, 5.9/2, 4.0/2]
MLmW_het_Jhigh=[]
MLmW_het_Jlow=[]
for i,t in enumerate(MLmW_dJ_het):
	MLmW_het_Jhigh.append(t + MLmW_het_dT[i])
	MLmW_het_Jlow.append(t - MLmW_het_dT[i])


# best fit of data
def linear(x,a,b):
	return a*x+b

popt_hom, pcov_hom = curve_fit(linear, [-100, -50, 1], MLmW_dJ, sigma=[(MLmW_Jhigh[0]-MLmW_Jlow[0])/2, (MLmW_Jhigh[1]-MLmW_Jlow[1])/2, (MLmW_Jhigh[2]-MLmW_Jlow[2])/2])
popt_het, pcov_het = curve_fit(linear, [-100, -50, 1], MLmW_dJ_het, sigma=MLmW_het_dT)


het_fit = []
for p in pressures:
	het_fit.append(popt_het[0]*p+popt_het[1])

het_hom_fit = []
for p in pressures:
	het_hom_fit.append(popt_hom[0]*p+popt_het[1])
	
hom_fit = []
for p in pressures:
	hom_fit.append(popt_hom[0]*p+popt_hom[1])


# best fit of our approximation (dT/dP = (Tm*dv)/lf)

slope_estimate = -0.069 #K/MPa
def intercept(x,b):
	return slope_estimate*x+b
	
popt_icpt_het, pcov_icpt_het = curve_fit(intercept, [-100, -50, 1], MLmW_dJ_het, sigma=MLmW_het_dT)
popt_icpt_hom, pcov_icpt_hom = curve_fit(intercept, [-100, -50, 1], MLmW_dJ, sigma=MLmW_dT)

estimate_fit_het = []
estimate_fit_hom = []
for p in pressures:
	estimate_fit_het.append(slope_estimate*p+popt_icpt_het[0])
	estimate_fit_hom.append(slope_estimate*p+popt_icpt_hom[0])


# best fit of melting line
popt_melt, pcov_melt = curve_fit(linear, [-100, -50, 1], MLmW_dmelt)


melt_fit = []
for p in pressures:
	melt_fit.append(popt_melt[0]*p+popt_melt[1])


print (popt_icpt_het, pcov_icpt_het)
print (popt_icpt_hom, pcov_icpt_hom)

print (popt_hom, pcov_hom)
print (popt_het, pcov_het)

print (popt_melt, pcov_melt)


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



plt.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'MLmW $T_{melt}$')
plt.plot(pressures, MLmW_dJ, '^g', linewidth=1.0, label=r'MLmW $J=10^{32} m^{-3}s^{-1}$')



plt.xlim(pmin, pmax)
plt.legend(loc='lower right')
plt.grid(color='#d4d4d4', linestyle='--', linewidth=1)

plt.tight_layout()
plt.savefig('plot_PT_delta_MLmW.png', dpi=300)


#--------------------
# Break y-axis

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
f.set(figwidth=5, figheight=6)

# plot melting data on both axis
ax.hlines(0, pmin, pmax, colors=['k'])
ax.text(pmin+5, -1.5, r'$T_{melt}$ at 0 MPa')

ax.plot(P_range, Mar_T(P_range)-273, '#707070', label=r'$T_{melt}$ from experiments (Marcolli, 2017)')
ax.plot(pressures, MLmW_dmelt, 'go', fillstyle='none', linewidth=1.0, label=r'$T_{melt}$ (Rosky et al., 2022)')
#ax.plot(pressures, melt_fit, 'g-', linewidth=1.0)

ax.plot(pressures, MLmW_dJ, 'bo', fillstyle='none', linewidth=1.0, label=r'$J_{hom}=10^{32}$ m$^{-3}$s$^{-1}$ (Rosky et al., 2022)')
ax.plot([-100, -50, 1], MLmW_dJ_het, 'ro', linewidth=1.0, label=r'$J_{het}=10^{24}$ m$^{-2}$s$^{-1}$')

# plot all data on second axis
#--- melting data

meltstr = '\n'.join((
    r'$T_{melt}$ from experiments',
    r'(Marcolli 2017)'))
    
ax2.plot(P_range, Mar_T(P_range)-273, '#707070', label=r'$T_{melt}$ from experiments (Marcolli 2017)')
ax2.plot(pressures, MLmW_dmelt, 'go', fillstyle='none', linewidth=1.0, label=r'$T_{melt}$ (Rosky 2022)')
#ax2.plot(pressures, melt_fit, 'g-', linewidth=1.0, label=r'Equilibrium melting point')

#--- freezing data



ax2.fill_between(pressures, MLmW_Jhigh, MLmW_Jlow, color='b', alpha=0.2)
ax2.plot(pressures, MLmW_dJ, 'bo', fillstyle='none', linewidth=1.0, label=r'$J_{hom}=10^{32}$ m$^{-3}$s$^{-1}$ (Rosky 2022)')
ax2.plot(pressures, estimate_fit_hom, 'b--', linewidth=1.0)

ax2.fill_between(pressures, MLmW_het_Jhigh, MLmW_het_Jlow, color='r', alpha=0.2)
ax2.plot([-100, -50, 1], MLmW_dJ_het, 'ro', linewidth=1.0, label=r'$J_{het}=10^{24}$ m$^{-2}$s$^{-1}$')
ax2.plot(pressures, estimate_fit_het, 'r--', linewidth=1.0)

#ax2.plot(pressures, het_fit, 'r--', linewidth=1.0, label=r'$J_{het}$ fit')
ax2.plot(pressures, het_fit, 'r-', linewidth=1.0)

#ax2.plot(pressures, hom_fit, 'b--', linewidth=1.0, label=r'$J_{hom}$ fit')
ax2.plot(pressures, hom_fit, 'b-', linewidth=1.0)



# Add text box to explain dashed and solid lines
props = dict(boxstyle='round', facecolor='white', alpha=1.0, edgecolor='#d4d4d4', pad=0.7)
textstr = '\n'.join((
    r'dashed lines = Equation 1',
    r'solid lines = best fit to data'))

# place a text box in upper left in axes coords
#ax2.text(30, -72, textstr, fontsize='small', verticalalignment='top', bbox=props)
        



# zoom-in / limit the view to different portions of the data
ax.set_ylim(-3., 10.)  # melting 
ax2.set_ylim(-85., -40.)  # homogeneous freezing

ax.set_xlim(pmin, pmax+5)
ax2.set_xlim(pmin, pmax+5)
#ax.legend(loc='upper right', fontsize='small')

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

ax.set_title('MLmW')
ax2.set_xlabel('Pressure (MPa)')
ax2.set_ylabel(r'T - T$_{melt}$')

'''
## get legend by itself
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.1, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
'''

plt.savefig('PT_diagram_MLmW_legend2.png', dpi=1000)


