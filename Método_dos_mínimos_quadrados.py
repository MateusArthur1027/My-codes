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
      return B1, B0, mx, my
    else:
        return print("Os vetores são de tamanhos diferentes")

resp = mínimos_quadrados(xi, yi, n)
print(f"\nB1 vale {resp[0]} e B0 vale {resp[1]}\n")
print(f"Resultando na equação y = {resp[1]} + ({resp[0]})*x\n")
def resíduos(y, x, resp):
  for i in x:
    B1xi = []
    B1xi.append(resp[0]*i)
  er = []
  er.append(y - (resp[1] + B1xi))
  return er

err = resíduos(yi, xi, resp)
def funres(x,resp):
  if np.isscalar(x) == True:
    ycc = resp[1] + (resp[0]*x)
    return ycc 
  else:
   ycc = []
   for i in x:
     j = resp[1] + (resp[0]*i)
     ycc.append(j)
   return ycc
yc = funres(xi, resp)
ycm = funres(resp[2], resp)
#Verificações:
if np.sum(err) == 0:
  print("A soma dos resíduos é zero\n")
else:
  print("A soma dos resíduos é diferente de zero\n")
if np.sum(yi) == np.sum(yc):
  print("A soma dos valores ajustados é a mesma da soma dos valors observados\n")
else:
  print("A soma dos valores ajustados é diferente da soma dos valores observados\n")
if ycm == resp[3]:
  print("A reta de regressão passa pelo centróide (xmédio, ymédio)\n")
else:
  print("A reta de regressão não passa pelo centróide(xmédio, ymédio)\n")
for i in yc:
  for j in err:
    sycerr = np.sum(i*j)
if sycerr == 0:
  print("A soma dos resíduos ponderados pelo valor correspondente ajustado é zero\n")
else:
  print("A soma dos resíduos ponderados pelo valor correspondente ajustado não é zero\n")  

plt.scatter(resp[2], resp[3], c='red')
plt.scatter(xi, yi)
plt.plot(xi, yc, c='orange')
plt.xlabel("Tempo(semanas)")
plt.ylabel("Propelente")
plt.show()
