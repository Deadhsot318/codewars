# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:23:51 2020

@author: suseel
"""


def get_count(input_str):
    """
    

    Parameters
    ----------
    input_str : TYPE
        DESCRIPTION. takes in a string

    Returns
    -------
    num_vowels : TYPE
        DESCRIPTION. counts the number of vowels in the string

    """
    num_vowels = 0
    tup_vowels = ('a', 'e', 'i', 'o', 'u')
    for i in tup_vowels:
        for j in input_str:
            if i == j:
                num_vowels += 1
    return num_vowels