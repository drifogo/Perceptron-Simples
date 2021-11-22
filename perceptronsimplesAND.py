import numpy as np
import time

def funcaoAtivacao(sout):
    if sout > 0:
        return 1
    else:
        return 0    

def somaPonderada(x,w):
    return np.dot(x,w)

#    bias   x1   x2
x = [[-1,   0,   0],
     [-1,   0,   1],
     [-1,   1,   0],
     [-1,   1,   1]]

# pesos
w = [1,1,1]

# taxa de aprendizado
eta = 0.6

# saídas desejadas
y = [0,
     0,
     0,
     1]

ciclo=1
sout=[]
erro=1
print("\nPesos iniciais:",w)
while erro==1:    
    erro = 0
    print("Ciclo:",ciclo)
    for amostras in range(len(x)): 
        sout = somaPonderada(x[amostras],w)
        print('Sout de x{}'.format(amostras),funcaoAtivacao(sout))
        if funcaoAtivacao(sout) != y[amostras]:
            erro = 1
            print("Sout de x{} diferente do esperado (y={})".format(amostras,y[amostras]))
            print("Ajustaremos os pesos...")
            for pesos in range(len(w)):
                w[pesos] = w[pesos] + (eta * ((y[amostras] - funcaoAtivacao(sout)) * x[amostras][pesos]))
            print("Novos pesos",w)
    ciclo+=1
    print("---------")
print("Ajuste concluído, pesos ótimos são:",w)