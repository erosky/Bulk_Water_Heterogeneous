import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Lines of constant J=10^27

pressures=[-100, -50, 1]
pmin = -120.0
pmax = 20.0
P_range=np.arange(pmin, pmax, 5)


mW_J=[209, 207.75, 205.5]
mW_dJ=[-64, -65.25, -67.5]
mW_dJ_th=[-65.3, -66.4, -67.5]
mW_melt=[275, 274, 273]
mW_dmelt=[2, 1, 0]


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


# homogeneous error bounds
mW_hom_Jhigh = []
mW_hom_Jlow = []
mW_hom_dT = [2.1, 1.9, 1.8]
for i,t in enumerate(mW_dJ):
	mW_hom_Jhigh.append(t + mW_hom_dT[i]/2)
	mW_hom_Jlow.append(t - mW_hom_dT[i]/2)
	
	
#################
# Data best fits
################
def linear(x,a,b):
	return a*x+b

popt_hom, pcov_hom = curve_fit(linear, [-100, -50, 1], mW_dJ, sigma=[(mW_hom_Jhigh[0]-mW_hom_Jlow[0])/2, (mW_hom_Jhigh[1]-mW_hom_Jlow[1])/2, (mW_hom_Jhigh[2]-mW_hom_Jlow[2])/2])

popt_het, pcov_het = curve_fit(linear, [-100, -50, 1], mW_dJ_het, sigma=mW_het_dT)


het_fit = []
for p in pressures:
	het_fit.append(popt_het[0]*p+popt_het[1])
	
hom_fit = []
for p in pressures:
	hom_fit.append(popt_hom[0]*p+popt_hom[1])


# best fit of our approximation (dT/dP = (Tm*dv)/lf)

slope_estimate = -0.022 #K/MPa
def intercept(x,b):
	return slope_estimate*x+b
	
popt_icpt_het, pcov_icpt_het = curve_fit(intercept, [-100, -50, 1], mW_dJ_het, sigma=mW_het_dT)
popt_icpt_hom, pcov_icpt_hom = curve_fit(intercept, [-100, -50, 1], mW_dJ, sigma=mW_hom_dT)

estimate_fit_het = []
estimate_fit_hom = []
for p in pressures:
	estimate_fit_het.append(slope_estimate*p+popt_icpt_het[0])
	estimate_fit_hom.append(slope_estimate*p+popt_icpt_hom[0])


# best fit of melting line
popt_melt, pcov_melt = curve_fit(linear, [-100, -50, 1], mW_dmelt)


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



#--------------------
# Break y-axis

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
f.set(figwidth=5, figheight=6)

# plot melting data on both axis
ax.hlines(0, pmin, pmax, colors=['k'])
ax.text(pmin+5, -1.5, r'$T_{melt}$ at 0 MPa')

ax.plot(P_range, Mar_T(P_range)-273, '#707070')
ax.plot(pressures, mW_dmelt,'go', fillstyle='none', linewidth=1.0)
#ax.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'MLmW $T_{melt}$')


# plot all data on second axis
#--- melting data
ax2.plot(P_range, Mar_T(P_range)-273, '#707070', label=r'$T_{melt}$ (Marcolli 2017)')
ax2.plot(pressures, mW_dmelt,'go', fillstyle='none', linewidth=1.0, label=r'$T_{melt}$ (Rosky 2022)')
#ax2.plot(pressures, MLmW_dmelt, 'go', linewidth=1.0, label=r'ML-mW $T_{melt}$')

#--- freezing data

# homogeneous
ax2.fill_between(pressures, mW_hom_Jhigh, mW_hom_Jlow, color='b', alpha=0.2)
ax2.plot(pressures, mW_dJ,'bo', fillstyle='none', linewidth=1.0, label=r'$J_{hom}=10^{32}$ m$^{-3}$s$^{-1}$ (Rosky 2022)')
ax2.plot(pressures, estimate_fit_hom, 'b--', linewidth=1.0)



#heterogeneous
ax2.fill_between(pressures, mW_het_Jhigh, mW_het_Jlow, color='r', alpha=0.2)
ax2.plot(pressures, mW_dJ_het, 'ro', linewidth=1.0, label=r'$J_{het}=10^{24}$ m$^{-2}$s$^{-1}$')
ax2.plot(pressures, estimate_fit_het, 'r--', linewidth=1.0)
#ax2.plot(pressures, mW_het_th,'r--', linewidth=1.0, label='Equation 1')



# plot best fit lines
ax2.plot(pressures, het_fit, 'r-', linewidth=1.0)
ax2.plot(pressures, hom_fit, 'b-', linewidth=1.0)



'''
ax2.fill_between(pressures, MLmW_Jhigh, MLmW_Jlow, color='g', alpha=0.2)
ax2.plot(pressures, MLmW_dJ, '^g', linewidth=1.0, label=r'ML-mW $J=10^{32}$ m$^{-3}$s$^{-1}$')
ax2.plot(pressures, MLmW_dJ_th, 'g--', linewidth=1.5, label='Equation 1')
'''






# zoom-in / limit the view to different portions of the data
ax.set_ylim(-3., 10.)  # melting 
ax2.set_ylim(-85., -40.)  # homogeneous freezing

ax.set_xlim(pmin, pmax+5)
ax2.set_xlim(pmin, pmax+5)
#ax2.legend(loc='lower right', fontsize='small')

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

ax.set_title('mW')
ax2.set_xlabel('Pressure (MPa)')
ax2.set_ylabel(r'T - T$_{melt}$')
plt.savefig('PT_diagram_mW_clean.png', dpi=1000)


