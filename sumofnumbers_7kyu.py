# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:39:08 2020

@author: suseel
"""
def get_sum(a,b):
    """
    

    Parameters
    ----------
    a : integer
    b : integer
    
    a and b are may not be in order

    Returns
    -------
    sum of all integers between a and b 

    """
    listsum = []
    if a < b:
        for i in range (a, b):
            listsum.append(i)
        listsum.append(b)
    else:
        for i in range(b, a):
            listsum.append(i)
        listsum.append(a)
    addlist = 0
    for i in listsum:
        addlist += i
    return addlist 

