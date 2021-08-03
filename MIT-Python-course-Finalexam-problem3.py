# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:01:16 2021

@author: Lenovo
"""

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for x in range(0, n):
        
        for y in range(0, n):
            
            for z in range(0, n):
                
                if 6 * x + 9 * y + 20 * z == n:
                    return True
    return False