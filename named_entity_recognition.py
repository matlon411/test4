# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:52:52 2021

@author: mathi
"""
import spacy as sC
nlp = sC.load('en_core_web_sm')

tokens3 = nlp('The book written by Hayden Liu in 2018 was sold at $30 in America')
print([(token_ent.text, token_ent.label_) for token_ent in tokens3.ents])