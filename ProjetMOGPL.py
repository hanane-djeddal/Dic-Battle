#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:01:40 2019

@author: liticia
"""
import numpy as np
from random import *
#
def strategieAveugle(D):
    d_opt=0
    EGopt=0
    for d in range(D):
        EG=((4*(d+1)-1)*((5/6)**(d+1))) +1
        if(EGopt<EG):
            d_opt=d+1
            EGopt=EG
    return d_opt

def constructionTableDynamique(N,D):
     cap=N-1+6*D
     tab=np.zeros([cap,cap,D])
     for i in range (N-1,cap):
         for j in range (cap):
             for d in range(0,D):#On considere que 0 vaut 1 dé
                 if(i>j):
                     tab[i][j][d]=1
                 elif(i==j):
                     tab[i][j][d]=0
                 else:
                     tab[i][j][d]=-1            
     for i in range(N-2,-1,-1):
        for j in range(cap-1,-1,-1):
            for d in range(0,D):
                for k in range(i+1,i+6*(d+1)):
                    tab[i][j][d]+=tab[k][j][d]
                tab[i][j][d]=(tab[i][j][d])*((5/6)**d)+(1-((5/6)**d))
     
     return tab

def strategieOptimale(N,D,i,j,tab):
    l=(list(tab[i][j]))
    d=l.index(max(l))
    return d+1
 
"""def constructionTableDynamique(N,D):
     cap=N-1+6*D
     tab=np.zeros([cap,cap])
     for i in range (N-1,cap):
         for j in range (cap):
             if(i>j):
                 tab[i][j]=1
             else:
                 tab[i][j]=0
     for i in range(N-2,-1,-1):
        for j in range(cap-1,-1,-1):
            for k in range(i+1,(i+6*D)):
                tab[i][j]+=tab[k][j]
            tab[i][j]=tab[i][j]/(6*D)
     return tab
 
def strategieOptimale(N,D,i,j,tab):
    l=(list(tab[:,j]))
    g=l.index(max(l))
    return int((g-i)/6)+1
"""
def simulation(N,D):
    #0: Strategie aveugle, 1:stratégie optimale
    result=np.empty([2,2])
    tab=constructionTableDynamique(N,D)
    for a in range (2):
        for b in range(2):
            #print("============== Nouvelle Partie: " )
            g1=0
            g2=0
            while ((g1< N) and (g2<N)):
                if (a == 0):
                    #print("Joueur 1 aveugle :")
                    d1=strategieAveugle(D)
                else :
                    #print("Joueur 1 optimale :")
                    d1=strategieOptimale(N,D,g1,g2,tab)
                for k in range (d1):
                    g=0
                    r=randint(1,6)
                    if (r == 1):
                        g=1
                        break
                    else:
                        g+=r
                g1+=g
                #print("Tour Joueur 1, lance : ",d1," dés, gain :",g1 )
                if (b == 0):
                    #print("Joueur 2 aveugle :")
                    d2=strategieAveugle(D)
                else :
                    #print("Joueur 2 optimale :")
                    d2=strategieOptimale(N,D,g2,g1,tab)
                for k in range (d2):
                    g=0
                    r=randint(1,6)
                    if (r == 1):
                        g=1
                        break
                    else:
                        g+=r
                g2+=g
                #print("Tour Joueur 2, lance : ",d2," dés, gain :",g2 )
            if (g1==g2):
                result[a][b]=0
                print("Nulle")
            if (g1<g2):
                result[a][b]=2
                print("Joueur 2 gagne")
            if (g1>g2):
                print("Joueur 1 gagne")
                result[a][b]=1
    return result
    
"""_________________________TESTS_______________________________"""   
N=10
D=3
tab=constructionTableDynamique(N,D)
print(tab)
#print(strategieAveugle(D))
#print(constructionTableDynamique(5,1))
#print(strategieOptimale(N,D,97,20,tab)) 
"""for i in range(10):
    print(simulation(100,i+1))

"""








