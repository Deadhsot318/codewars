# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:30:10 2020

@author: suseel
"""
def DNA_strand(dna):
# =============================================================================
# In DNA strings, symbols "A" and "T" are complements of each other, 
# as "C" and "G". You have function with one side of the DNA 
# (string, except for Haskell); you need to get the other complementary side.
# =============================================================================
    a = [ ]
    for i in dna:
        if i =='A':
            a.append('T')
        elif i =='T':
            a.append('A')
        elif i =='C':
            a.append('G')
        else:
            a.append('C')
    return ''.join(a)

