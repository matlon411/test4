# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:04:27 2021

@author: mathi
"""

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer() # Indfører functionen, så vi kan tage den på noget andet
g = porter_stemmer.stem('machines') # Choosing the method stem function.
print(g) # When we stem stuff, we just take the word and make it its lowest component

# Now we can do lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('machines'))