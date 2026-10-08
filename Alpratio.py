import matplotlib.pyplot as plt
import numpy as np

#below is GEANT4 simulation of ALPs simulation 

ALP_produced_ratio_to_lead = [1 , 0.335154827 , 1.58287796 , 0.361566485 , 0.661202186] #ALP produced

Error_associated_to_lead = [0, 0.061,0.19,0.06 , 0.103]

#####

ALPs_production_theortical_ratio = [1, 0.28826946 , 1.571307595 , 0.29371734 , 0.615196786, 0.43563989 ,0.332585052, 0.225539415]

Z = [82 ,26 ,74 ,30 ,47 ,50 ,40 ,56 ]


# This is updated after running 1 million events 

ALP_produced_ratio_to_lead = [1 , 0.299234579 , 1.562449347 , 0.304007204 , 0.63241783 , 0.443133724 , 0.346150383 ,0.229716344] #ALP produced

Error_associated_sim = [0 ,0.006 ,0.02 ,0.006 ,0.007 ,0.007 ,0.006 ,0.005]



plt.figure()

# Plot experimental data with error bars
plt.errorbar(Z, ALP_produced_ratio_to_lead, yerr=Error_associated_sim, fmt='o', capsize=5, label='GEANT4 simulation')
plt.errorbar(Z, ALPs_production_theortical_ratio, fmt='o', capsize=5, label='Theory')


plt.xlabel('Z of material')
plt.ylabel('Ratio of ALPs produced to lead')
plt.title('Ratio check for ALPs between theory and simulation')

plt.yscale('log')
plt.legend()

plt.savefig("Alpratio.png", dpi=300, bbox_inches='tight')

plt.show()




### -------------------------------------------------------------  ### 

ALP_sim = [
    1.1105E-08,
    3.323E-09,
    1.7351E-08,
    3.376E-09,
    7.023E-09,
    4.921E-09,
    3.844E-09,
    2.551E-09
]

ALP_sim_error = [
    1.0538E-10,
    5.76455E-11,
    1.31723E-10,
    5.81034E-11,
    8.38033E-11,
    7.01498E-11,
    6.2E-11,
    5.05074E-11
]

theory = [
    1.12502E-08,
    3.24308E-09,
    1.77005E-08,
    3.30437E-09,
    6.92106E-09,
    4.90102E-09,
    3.74164E-09,
    2.53735E-09
]


plt.figure()

# Plot experimental data with error bars
plt.errorbar(Z, ALP_sim, yerr=ALP_sim_error, fmt='o', capsize=5, label='Simulation')
plt.errorbar(Z, theory, fmt='o', capsize=5, label='Theory')


plt.xlabel('Z of material')
plt.ylabel('Probability of ALPs being produced')
plt.title('Comparison of Probability of ALPs being produced for theory and simulation')

plt.yscale('log')
plt.legend()

plt.savefig("Al_probability.png", dpi=300, bbox_inches='tight')

plt.show()


plt.figure()

ALP_100k = np.array([20916, 5489, 20805, 5563, 16595, 11441, 7166, 2976])

ALP_100k_no_shower = np.array([1110.5, 332.3, 1735.1, 337.6, 702.3, 492.1, 384.4, 255.1])

plt.plot(Z, ALP_100k, 'o', label='With showering')

plt.plot(Z, ALP_100k_no_shower, 'o', label='Without showering')

plt.xlabel('Z of material')
plt.ylabel('Raw number of ALPs being produced')

plt.title('Comparison of ALPs being produced with showering turned on')
plt.yscale('log')

plt.legend()

plt.savefig("Enhancement.png", dpi=300, bbox_inches='tight')

plt.show()


plt.figure()

Enhancement = ALP_100k/ALP_100k_no_shower

plt.plot(Z, Enhancement, 'x')
#plt.plot(Z, ALP_100k_no_shower, 'o', label='Without showering')

plt.xlabel('Z of material')
plt.ylabel('Ratio of enhancement')

plt.title('Ratio of enhancement of showering')
#plt.yscale('log')

#plt.legend()

plt.savefig("Enhancement_ratio.png", dpi=300, bbox_inches='tight')

plt.show()


ALP_100MeV = np.array([3024.6,
1361.3,
2520.104167,
1364.7,
2799.3,
2183.9,
1596,
780.7])


ALP_1GeV= np.array([41.5
,40.7
,0
,38.7
,41.7
,41.2
,37.6
,30.8])



plt.figure()

plt.plot(Z, ALP_1GeV, '.', label='1 GeV ALP 0.001 [1/GeV]')
plt.plot(Z, ALP_100MeV, 'x', label='100 MeV ALP 0.001 [1/GeV]')
plt.plot(Z, ALP_100k, 'o', label='16.7 MeV ALP 0.001 [1/GeV]')

plt.xlabel('Z of material')
plt.ylabel('ALPs produced')

plt.title('ALP production with different mass parameters')
plt.yscale('log')

plt.legend()

plt.savefig("ALPS_DifferentParam.png", dpi=300, bbox_inches='tight')

plt.show()



