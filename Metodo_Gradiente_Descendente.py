import sympy as sp
import numpy as np

x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')
lab = sp.Symbol('lab')

f = ((x1 - 2)**4) + ((x1 - 2*x2)**2)

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

def Metodo_Grad_Descendente(fun, E, y, lab, it):
    gr = Grad(fun,y)
    normgrad = np.linalg.norm(np.array(gr, dtype=float))
    i=0
    while normgrad > E and i < it:
        d = (-gr/normgrad)
        etp = etapa(y, d, lab)
        faux = f_univar(fun,etp)
        labaux = solucao_univar_newtow(faux, lab)
        y = [float(y[0] + labaux*d[0]), float(y[1] + labaux*d[1])]
        gr = Grad(fun,y)
        normgrad = np.linalg.norm(np.array(gr, dtype=float))
        i += 1


    return y, i

it = 10
E = 0.001
y = [0, 3]
resp, ctd = Metodo_Grad_Descendente(f, E, y, lab, it)
print(f"Após {ctd} iterações, o ponto mínimo é {resp}")
