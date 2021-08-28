# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:16:02 2021

@author: mathi
"""

from sklearn.datasets import fetch_20newsgroups
import numpy as np
groups = fetch_20newsgroups()

# Now showing the 5 different keys
groups.keys()
print(groups.keys())
print('\n')
# now it shows the different features one can tagke, so lets see on the target names
print(groups['target_names'])
print('\n')
print(groups.target)
print('\n')
print(np.unique(groups.target))

# benytter nu seaborn til at se på fordelingen af artikler, kategorier
# Det er nemmest at have lige mange af hver

import seaborn as sms
sms.distplot(groups.target)

print(groups.data[0])