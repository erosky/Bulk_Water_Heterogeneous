# DATE: 2022-03-25 
# CONTRIBUTOR: Elise Rosky, emrosky@mtu.edu 
# CITATIONS: 
# Molinero and Moore,  J Phys Chem, 113, 4008-4016, (2009); 
# Chan et. al., Nat Comm, (2019), https://doi.org/10.1038/s41467-018-08222-6;
# Lupi et al., JACS, (2014)

# Stillinger-Weber parameters for modeling water - ML-mW model
# Including "two-body SW potential" for substrate-water interactions
# Where C represents a hydrophilic substrate molecule interacting with MLmW water molecules

# The first element in the entry is the center atom in a three-body interaction. Thus an entry for mWCC means a mW atom with 2 C atoms as neighbors. 
# The parameter values used for the two-body interaction come from the entry where the second and third elements are the same. Thus the two-body parameters for mW interacting with C, comes from the mWCC entry. 

# these entries are in LAMMPS "real" units:
#   epsilon = Kcal/mole; sigma = Angstroms
#   other quantities are unitless

# format of a single entry (one or more lines):
#   element 1, element 2, element 3, 
#   epsilon, sigma, a, lambda, gamma, costheta0, A, B, p, q, tol

# The A, B, p, and q parameters are used only for two-body interactions. The lambda and costheta0 parameters are used only for three-body interactions. The epsilon, sigma and a parameters are used for both two-body and three-body interactions. gamma is used only in the three-body interactions, but is defined for pairs of atoms

# ALL PARAMETERS FOR mW-C ARE THE SAME AS FOR MLmW-MLmW INTERACTION, in real units from Chan et. al., Nat Comm, (2019)
# EXCEPT FOR epsilon AND sigma, which have been adjusted by Elise Rosky to create a hydrophilic interaction between mW and C


mW mW mW 	6.855473	1.884015	2.124872	24.673877  	1.207943  	-0.279667  		7.111598  	1.991526  	4.011214  	0.0 0.0
         
mW C C		0.35	2.2	2.124872	0.0		1.207943	-0.279667		7.111598	1.991526	4.011214 	0.0 0.0

C mW mW  	0.35	2.2	2.124872	0.0		1.207943	-0.279667		7.111598	1.991526	4.011214 	0.0 0.0
         
C mW C		0.0  		1.0  		0.0  		0.0  		0.0  		-0.279667	  	0.0  		0.0  		0.0  		0.0 0.0
         
C C mW		0.0  		1.0  		0.0  		0.0  		0.0  		-0.279667	  	0.0  		0.0  		0.0  		0.0 0.0
         
mW mW C  	0.0  		1.0  		0.0  		0.0  		0.0  		-0.279667	  	0.0  		0.0  		0.0  		0.0 0.0
         
mW C mW  	0.0  		1.0  		0.0  		0.0  		0.0  		-0.279667	  	0.0  		0.0  		0.0  		0.0 0.0

C  C  C	0.0  		1.0  		0.0  		0.0  		0.0  		-0.279667	  	0.0  		0.0  		0.0  		0.0 0.0 


