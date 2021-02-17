import matplotlib.pyplot as plt
import numpy as np

k = np.arange(1,10**3+1)
ek1 = np.array([0.5/(i**.5) for i in k])
ek2 = np.array([(0.5/i) for i in k])
ek3 = np.array([(0.5/(i*i)) for i in k])

# Plots i - iii
plt.plot(k, ek1, label=r"$e_k=\frac{0.5}{\sqrt{k}}$")
plt.plot(k, ek2, label=r"$e_k=\frac{0.5}{k}$")
plt.plot(k, ek3, label=r"$e_k=\frac{0.5}{k^2}$")
plt.legend(loc="upper right")
plt.xscale('log')
plt.yscale('log')
plt.ylabel(r'$e_k$')
plt.xlabel('k')
plt.title('Sublinear Convergence')
plt.show()

ek4 = []
ek4.append(0.5)
print(ek4)
for i in range(10**3-1):
    ek4.append(.975*ek4[i])

ek4 = np.array(ek4)
plt.plot(k, ek4, label=r"$e_1=0.5, e_k=0.975e_{k-1}, k\geq2$")
plt.legend(loc="upper right")
plt.yscale('log')
plt.ylabel(r'$e_k$')
plt.xlabel('k')
plt.title('Linear Convergence')
plt.show()

ek5 = []
ek5.append(0.5)
for i in range(10**2-1):
    ek5.append(1.9*ek5[i]**2)

ek5 = np.array(ek5)
plt.plot(k[0:100], ek5, label=r"$e_1=0.5, e_k=1.9e_{k-1}^2, k\geq2$")
plt.legend(loc="upper right")
plt.yscale('log')
plt.ylabel(r'$e_k$')
plt.xlabel('k')
plt.title('Quadratic Convergence')
plt.show()
