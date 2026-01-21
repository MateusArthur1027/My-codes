import numpy as np
import matplotlib.pyplot as plt

L = 1
u = 0.1
n = 101
temp_ini = 20
delt = 0.05
t_total = 5
delx = L/(n-1)
x = np.linspace(0, L, n)
MAXVAL = 1e300  # evita overflow

def MDF_eqtransporte(n, delt, delx, u, temp_ini, t_total, x):
    c = (u*delt)/delx
    T = np.full(n, temp_ini)
    T[0] = 100
    vecplot = [0, 1, 2, 3, 4, 5]
    t = 0
    while t <= t_total - 1e-50:
      for j in vecplot:
         if abs(t-j) < 1e-6:   
           plt.plot(x, T, label = f"t={t:.1f}s")
      T_old = T.copy()
      for i in range(n):
          if i == 0:
            T[i] = 100
          elif i == n-1:
            T[i] = T_old[i-1]
          else:
            T[i] = T_old[i] - c*(T_old[i] - T_old[i-1])
          # impedir overflow
            if abs(T[i]) > MAXVAL:
                T[i] = np.sign(T[i]) * MAXVAL
   
      t += delt


 
MDF_eqtransporte(n, delt, delx, u, temp_ini, t_total, x)

plt.xlabel("Nós (x)")
plt.ylabel("Temperatura (°C)")
plt.title("Relação temperatura por nó em cada instante de tempo")
plt.grid(True)
plt.legend()
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(13,5))

# Estável
plt.sca(axs[0])
MDF_eqtransporte(n, 0.1, delx, u, temp_ini, t_total, x)
axs[0].set_title("Estável — Δt = 0.10s")
axs[0].set_xlabel("Nós (x)")
axs[0].set_ylabel("Temperatura (°C)")
axs[0].grid(True)
axs[0].legend()

# Instável
plt.sca(axs[1])
MDF_eqtransporte(n, 0.2, delx, u, temp_ini, t_total, x)
axs[1].set_title("Instável — Δt = 0.15s")
axs[1].set_xlabel("Nós (x)")
axs[1].set_ylabel("Temperatura (°C) - na escala logarítmica ")
axs[1].set_yscale("log")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()


