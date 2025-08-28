import matplotlib.pyplot as plt
import numpy as np

xi = [15.5, 23.75, 8, 17, 5.5, 19, 24, 2.5, 7.5, 11, 13, 3.75, 25, 9.75, 22, 18,
      6, 12.5, 2, 21.5]
yi = [2158.7, 1678.15, 2316, 2061.3, 2207.5, 1708.3, 1784.7, 2575,2357.9, 2256.7, 
      2165.2, 2399.55, 1779.8, 2336.75, 1765.3, 2053.5, 2414.4, 2200.5, 2654.2, 1753.7]
n = len(xi)
def mínimos_quadrados(xi, yi, n):
    if len(xi) == len(yi):
      sxi = np.sum(xi)
      syi = np.sum(yi)
      vec2 = np.full(n,2)
      sxi2 = np.sum(pow(xi,vec2))
      xiyi = np.multiply(xi, yi)
      sxiyi = np.sum(xiyi)
      my = syi/n
      mx = sxi/n
      B1 = (sxiyi - ((sxi*syi)/n))/(sxi2 - ((sxi**2)/n))
      B0 = my - (B1*mx)
      return B1, B0
    else:
        return print("Os vetores são de tamanhos diferentes")

resp = mínimos_quadrados(xi, yi, n)
print(f"\nB1 vale {resp[0]} e B0 vale {resp[1]}\n")
print(f"Resultando na equação y = {resp[1]} + ({resp[0]})*x\n")

def resíduos(resp, xi, yi):
  B1xi = []
  for i in xi:
    B1xi.append(resp[0]*i)
  er = yi -(resp[1] + B1xi)
  return er

eixoy = np.array(resíduos(resp, xi, yi))
eixox = np.arange(len(eixoy))
plt.scatter(eixox, eixoy)
plt.xlabel("Posição(i)")
plt.ylabel("Valor do resíduo")
plt.title("Valor do resíduo por posição (i) de xi e yi")
plt.show()