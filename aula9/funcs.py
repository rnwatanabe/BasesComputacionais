import numpy as np

def regressao(x, y):
    '''
    Calcula a inclinação m ep intercepto b da reta de regressão utilizado o método dos 
    mínimos quadrados. 
    
    Parâmetros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    m: float
       inclinação da reta de regressão
       
    b: float
       intercepto da reta de regressão
    '''
    m = mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    m = np.sum(desvioX*desvioY)/np.sum(desvioX**2)
    b = mediaY - m*mediaX
    
    return m, b