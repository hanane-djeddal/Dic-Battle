#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:01:40 2019

@author: Touzari Liticia
@author : Djeddal Hanane
"""
import strategies as st


"""____________________________M A I N_______________________________"""   
N=50
D=10

#_____________Prg Dynamique Séquentielle
#P=st.constructionMatrice_P(D)
#tab,strat=st.constructionTableDynamique(N,D,P)

#print(strat)
#print(st.strategieAveugle(D))
#print(st.strategieOptimale(80,3,strat)) 

#_____________Simulation Séquentielle
#print(st.simulation(N,D))
#print(st.calculEsperanceGain_N(D))


#_____________Prg linéaire Simultanée
#EG=st.constructionEG(D,P)
#print(st.resolutionPL(D,EG))

#_____________Simulation Simultanée
g1,g2=st.test_S_vs_A(D)
print("Esperance du gain Joeur 1 (optimale) :",g1, ". Esperance du gain Joeur 2 (aveugle) :",g2)


#_____________Prg Dynamique Simultanée
#EG2,strat=st.construction_EG_General(N,D,P)
#evalEG=st.calculEsperanceGainGeneral_N(D)
#print(evalEG)