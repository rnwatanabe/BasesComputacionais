# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:10:05 2019

@author: marcus.bonifacio
"""

import numpy as np

def regressao(x, y):
    '''
    Calcula a inclinação m e o intercepto b da reta de regressÃ£o utilizado o mÃ©todo dos 
    mÃ­nimos quadrados. 
    
    ParÃ¢metros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    m: float
       inclinaÃ§Ã£o da reta de regressÃ£o
       
    b: float
       intercepto da reta de regressÃ£o
    '''
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    m = np.sum(desvioX*desvioY)/np.sum(desvioX**2)
    b = mediaY - m*mediaX
    
    return m, b



def corr(x, y):
    '''
    Calcula o coeficiente de correlação
    
    Parâmetros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    r: float
        coeficiente de correlação
    '''
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    varX = np.sqrt(np.sum(desvioX**2))
    varY = np.sqrt(np.sum(desvioY**2))
    r = np.sum(desvioX*desvioY)/(varX*varY)
    
    return r

















