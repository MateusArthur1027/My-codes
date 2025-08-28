import matplotlib.pyplot as plt
import numpy as np
def fun(x):
    return (x**2) - (2*x) + 3 
    

def seccao_aurea(fi, xh, xl, E):
    x1 = xh - fi*(xh - xl)
    x2 = xl + fi*(xh - xl)
    i = 0 
    x1_lista = [x1]
    x2_lista = [x2]
    while abs(x1 - x2) > E:
        
        if fun(x1) < fun(x2):
         xh = x2
         i += 1
        elif fun(x1) > fun(x2):
         xl = x1
         i += 1
        else: 
         return (x1 + x2)/2 , i, x1_lista, x2_lista 
        x1 = xh - fi*(xh - xl)
        x2 = xl + fi*(xh - xl)
        x1_lista.append(x1)
        x2_lista.append(x2)
    return (x1 + x2)/2 , i, x1_lista, x2_lista
       
    
fi = 0.618
xh = 3
xl = -2
E = 0.1
resp, itra, x1_valores, x2_valores = seccao_aurea(fi, xh, xl, E)
print(f"O ponto de mínimo da função é {resp} após {itra} iterações")

media_x1_x2=[]

for j in range(len(x1_valores)):
    m = (x1_valores[j] + x2_valores[j])/2
    media_x1_x2.append(m)
 
eixoy = np.array(media_x1_x2)
eixox = np.arange(len(eixoy))
plt.scatter(eixox, eixoy)
plt.xlabel("Iterações")
plt.ylabel("Média de X1 e X2")
plt.title("Média de X1 e X2 por iteração")
plt.show()