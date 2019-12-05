#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:01:40 2019

@author: liticia
"""
import numpy as np
from random import *
#

def constructionMatrice_Q(D):
    Q=np.zeros([D+1,6*(D+1)])

    for k in range(2,7):#d=1
        Q[1][k]=1/5
    for d in range(1,D+1):
        Q[d][1]=0
        for k in range(2, 2*d):
            Q[d][k]=0
        for k in range(6*d+1,6*(D+1)):
            Q[d][k]=0
    for d in range(2,D+1):
        for k in range(2*d,6*d+1):
            for j in range(2,7):
                Q[d][k]+=Q[d-1][k-j]
            Q[d][k]=Q[d][k]/5
    return Q

def constructionMatrice_P(D):
    Q=constructionMatrice_Q(D)
    P=np.zeros([D+1,6*(D+1)])
    for d in range(1,D+1):
        P[d][1]=1-(5/6)**(d)
        for k in range(2, 2*d):
            P[d][k]=0
        for k in range(6*d+1,6*(D+1)):
            P[d][k]=0
        for k in range(2*d,6*d+1):
            P[d][k]=Q[d][k]*((5/6)**(d))
    return P
def strategieAveugle(D):
    d_opt=0
    EGopt=0
    for d in range(D):
        EG=((4*(d+1)-1)*((5/6)**(d+1))) +1
        if(EGopt<EG):
            d_opt=d+1
            EGopt=EG
    return d_opt   
"""def constructionTableDynamique(N,D):
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
     
     return tab"""
"""     
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
                    tab[i][j][d]+=((tab[k][j][d])*((5/6)**d)-(1-((5/6)**d)))
                tab[i][j][d]=tab[i][j][d]
     return tab   """
def constructionTableDynamique(N,D):
     P=constructionMatrice_P(D)
     cap=N-1+6*D
     tab=np.zeros([cap+1,cap+1,D+1])
     for i in range (N,cap+1):
         for j in range (cap+1):
             for d in range(1,D+1):#On considere que 0 vaut 1 dé
                 if(i>j):
                     tab[i][j][d]=1
                 elif(i==j):
                     tab[i][j][d]=0
                 else:
                     tab[i][j][d]=-1      
     for j in range (N,cap+1):
         for i in range (N):
             for d in range(1,D+1):
                 if(i>j):
                     tab[i][j][d]=1
                 elif(i==j):
                     tab[i][j][d]=0
                 else:
                     tab[i][j][d]=-1      
     for i in range(N-1,0,-1):
        for j in range(N-1,0,-1):
            for d in range(1,D+1):
                t=0
                for k in range(1,6*d+1):
                    #tab[i][j][d]+= (1-(sum(tab[j+k][i])/d))*P[d][k]
                    tab[i][j][d]+= (-sum(tab[j+k][i])/d)*(1-P[d][k])+(P[d][k])*(sum(tab[j+k][i])/d)
     return tab
 
def strategieOptimale(N,D,i,j,tab):
    l=(list(tab[i][j]))
    d=l.index(max(l))
    return d+1
def strategieAleatoire(D):
    return randint(1, D)
 
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
            print("============== Nouvelle Partie: N=",N,' D=',D )
            if(a==0):
                print("Joueur 1 aveugle :")
            else:
                print("Joueur 1 optimale :")
            if(b==0):
                print("Joueur 2 aveugle :")
            else:
                print("Joueur 2 optimale :")
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
    
def simulationGain(tab,N,D,s1,s2):#s1,s2= 0: Strategie aveugle, 1:stratégie optimale 2:stratégie aléatoire
    g1=0
    g2=0
    while ((g1< N) and (g2<N)):
        if(s1 == 0):
            d1=strategieAveugle(D)
        if(s1 == 1):
            d1=strategieOptimale(N,D,g1,g2,tab)
        if(s1 == 2):
            d1=strategieAleatoire(D)
        for k in range (d1):
            g=0
            r=randint(1,6)
            if (r == 1):
                g=1
                break
            else:
                g+=r
        g1+=g
            
        if(s2 == 0):
            d2=strategieAveugle(D)
        if(s2 ==1 ) :
            d2=strategieOptimale(N,D,g2,g1,tab)
        if(s2 == 2):
            d2=strategieAleatoire(D)
        for k in range (d2):
            g=0
            r=randint(1,6)
            if (r == 1):
                g=1
                break
            else:
                g+=r
        g2+=g
                
    joueur1=0
    joueur2=0
    if (g1<g2):
        joueur2=1
    if (g1>g2):
        joueur1=1
    return joueur1, joueur2
              
            
def calculEsperanceGain_D(N,D):
    tab=constructionTableDynamique(N,D)
    nb_parties=10
    A_O_1=[]
    A_O_2=[]
    O_A_1=[]
    O_A_2=[]
    A_A_1=[]
    A_A_2=[]
    O_O_1=[]
    O_O_2=[]
    A_R_1=[]
    A_R_2=[]
    R_O_1=[]
    R_O_2=[]
    
    print("aveugle vs optimale")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,0,1)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        A_O_1.append(G1/nb_parties)
        A_O_2.append(G2/nb_parties)
    print("\n optimale vs aveugle")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,1,0)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (optimale) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (aveugle) : ",G2/nb_parties)
        O_A_1.append(G1/nb_parties)
        O_A_2.append(G2/nb_parties)
    print("\n aveugle vs aveugle")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,0,0)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (aveugle) : ",G2/nb_parties)
        A_A_2.append(G1/nb_parties)
        A_A_2.append(G2/nb_parties)
    print("\n optimale vs optimale")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,1,1)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (optimale) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        O_O_1.append(G1/nb_parties)
        O_O_2.append(G2/nb_parties)
        
    print("\n random vs optimale")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,2,1)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (random) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        R_O_1.append(G1/nb_parties)
        R_O_2.append(G2/nb_parties)
        
    print("\n aveugle vs random")
    G1=0
    G2=0
    for d in range(1,D+1):
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,N,d,0,2)
            G1+=g1
            G2+=g2
        print("D :",d)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (random) : ",G2/nb_parties)
        A_R_1.append(G1/nb_parties)
        A_R_2.append(G2/nb_parties)
    
    return A_O_1, A_O_2, O_A_1, O_A_2, A_A_1, A_A_2, O_O_1, O_O_2, A_R_1, A_R_2, R_O_1, R_O_2

def calculEsperanceGain_N(D):
    A_O_1=[]
    A_O_2=[]
    O_A_1=[]
    O_A_2=[]
    A_A_1=[]
    A_A_2=[]
    O_O_1=[]
    O_O_2=[]
    A_R_1=[]
    A_R_2=[]
    R_O_1=[]
    R_O_2=[]
    nb_parties=10
    for n in range(50,250,50): 
        tab=constructionTableDynamique(n,D)
        print("aveugle vs optimale")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,0,1)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        A_O_1.append(G1/nb_parties)
        A_O_2.append(G2/nb_parties)
        
        print("\n optimale vs aveugle")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,1,0)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (optimale) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (aveugle) : ",G2/nb_parties)
        O_A_1.append(G1/nb_parties)
        O_A_2.append(G2/nb_parties)
        
        print("\n aveugle vs aveugle")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,0,0)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (aveugle) : ",G2/nb_parties)
        A_A_2.append(G1/nb_parties)
        A_A_2.append(G2/nb_parties)
        
        print("\n optimale vs optimale")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,1,1)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (optimale) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        O_O_1.append(G1/nb_parties)
        O_O_2.append(G2/nb_parties)
        
        print("\n random vs optimale")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,2,1)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (random) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (optimale) : ",G2/nb_parties)
        R_O_1.append(G1/nb_parties)
        R_O_2.append(G2/nb_parties)
        
        print("\n aveugle vs random")
        G1=0
        G2=0
        for i in range(nb_parties):
            g1,g2=simulationGain(tab,n,D,2,1)
            G1+=g1
            G2+=g2
        print("N :",n)
        print("Esperance de gain du joueur 1 (aveugle) : ",G1/nb_parties)
        print("Esperance de gain du joueur 2 (random) : ",G2/nb_parties)
        A_R_1.append(G1/nb_parties)
        A_R_2.append(G2/nb_parties)
        
    
    return A_O_1, A_O_2, O_A_1, O_A_2, A_A_1, A_A_2, O_O_1, O_O_2, A_R_1, A_R_2, R_O_1, R_O_2 


    
"""_________________________TESTS_______________________________"""   
N=200
D=5
#tab=constructionTableDynamique(N,D)
#print(tab)
#print(strategieAveugle(D))
#print(constructionTableDynamique(5,1))
#print(strategieOptimale(N,D,97,20,tab)) 
#print(calculEsperanceGain_N(D))

#print(simulation(N,D))








