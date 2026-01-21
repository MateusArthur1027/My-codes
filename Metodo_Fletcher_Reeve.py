import sympy as sp
import numpy as np

x1, x2, lab = sp.symbols('x1, x2, lab')

f = ((x1 - 2)**4) +((x1-2*x2)**2)

def Grad(fun, p):
    gra = sp.Matrix([sp.diff(fun, x1), sp.diff(fun, x2)])
    Gradf = sp.lambdify((x1,x2), gra,'numpy')
    grad = np.array(Gradf(p[0], p[1]), dtype=float).flatten()
    return grad

def etapa(y, d, var):
    return [y[0]+var*d[0], y[1]+var*d[1]]

def f_univar(fsimb, y):
    return fsimb.subs({x1:y[0], x2:y[1]})

def solucao_univar_newtow(fun, var):
    dr1 = sp.diff(fun, var)
    dr2 = sp.diff(dr1, var)
    f1_num = sp.lambdify(var, dr1, 'numpy')
    f2_num = sp.lambdify(var, dr2, 'numpy')
    if dr1 is not None and dr2 is not None:
        x0 = 0.00
        E = 0.001
        max_inter = 6
        for _ in range(max_inter):
         d1 = f1_num(x0)
         d2 = f2_num(x0)
         if abs(d2) < 1e-12:
          break
         x1 = x0 - d1/d2
         if abs(x1 - x0) < E:
          return x1
         x0 = x1
        return x0

def Metodo_Fletcher_Reeves(f, y0, E, lab):
    normgrad = np.linalg.norm(np.array(Grad(f,y0), dtype=float))
    i = 0
    while normgrad > E:
     d0 = -1*(Grad(f,y0))
     etp = etapa(y0, d0, lab)
     fauxi = f_univar(f,etp)
     labaux = solucao_univar_newtow(fauxi, lab)
     y1 = [float(y0[0]+labaux*d0[0]), float(y0[1]+labaux*d0[1])]
     normagrad1=np.linalg.norm(np.array(Grad(f,y0), dtype=float))
     normagrad2=np.linalg.norm(np.array(Grad(f,y1), dtype=float))
     alfa = (normagrad2**2)/(normagrad1**2)
     d0 = -1*(Grad(f,y1))+(alfa*d0)
     etp = etapa(y1, d0, lab)
     fauxi = f_univar(f,etp)
     labaux = solucao_univar_newtow(fauxi, lab)
     y0 = [float(y1[0]+labaux*d0[0]), float(y1[1]+labaux*d0[1])]
     normgrad = np.linalg.norm(np.array(Grad(f,y0), dtype=float))
     i += 1

    return y0, i


y0 = [0, 3]
E = 0.0001
resp, ctd = Metodo_Fletcher_Reeves(f, y0, E, lab)
print(f"Após {ctd} iterações, o ponto mínimo é {resp}")