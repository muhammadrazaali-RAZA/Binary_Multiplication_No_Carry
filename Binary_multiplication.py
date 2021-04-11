# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:54:41 2021

@author: Raza_Jutt
"""

def binary_multiply_no_carry(ary1,ary2):
    ary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ary1.reverse()
    ary2.reverse()
    for i in range(0,len(ary1)):
        for j in range(0,len(ary2)):
            ary[i+j]= ary[i+j] + (ary1[i]*ary2[j])
    print(ary)
    ary = ary[:8]
    ary.reverse()
    for i in range(0,len(ary)):
        if ary[i]%2==0:
            ary[i]=0
        else:
            ary[i]=1
    return ary
      
    
print(binary_multiply_no_carry([0,0,0,0,0,0,1,1],[1,0,1,0,0,0,0,0]))