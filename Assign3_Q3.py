# -*- coding: utf-8 -*-
"""
@author: user
"""

#calling dataset using pandas
import pandas as pd
import numpy as np
from scipy import stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2

#Importing Files
df = pd.read_csv("BuyerRatio.csv")
df

#Observed Values
table = [[50,142,131,70],
        [435,1523,1356,750]]


#Applying Chi-Square contingency table to convert observed value into expected value
stat, p, dof, expected = stats.chi2_contingency(table)
print("stat=",stat)
print("p_value=",p)
print("Degrees of freedon=",dof)
print("Expected Values=",expected)

observed = np.array([50, 142, 131, 70, 435, 1523, 1356, 750])
expected = np.array([42.76531299,  146.81287862,  131.11756787, 72.30424052, 442.23468701, 1518.18712138, 1355.88243213, 747.69575948])

#Compare Evidences with Hypothesis using t-statictic
test_statistic , p_value = stats.chisquare(observed, expected,dof)
print("Test Statistic = ",test_statistic,'\n', 'p_value =',p_value)

alpha = 0.05

print('significance=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
	print("Ho is rejected & H1 is accepted")
else:
	print("H0 is accepted & H1 is rejected")