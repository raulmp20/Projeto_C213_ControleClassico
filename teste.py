from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
mat = loadmat('TransferFunction15.mat')

degrau = mat['degrau']
saida = mat['saida']
t1 = mat['t']

plt.plot(t1.T, saida, label='Saída')
plt.plot(t1.T, degrau, label='Degrau de entrada')
plt.xlabel('t [s]')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")

# Inicialize t_63_2 com um valor padrão de -1
t_63_2 = -1

# Encontre o valor de t correspondente a 63,2% da amplitude máxima da saída
amplitude_max = max(saida)
threshold = 0.632 * amplitude_max

for i in range(len(t1)):
    if saida[i] >= threshold:
        t_63_2 = t1[i][0]
        break

if t_63_2 != -1:
    plt.axvline(x=t_63_2, color='r', linestyle='--', label=f'63.2% at t = {t_63_2:.2f}s')
    plt.legend()
    print(f'O valor de t correspondente a 63.2% da amplitude máxima é {t_63_2:.2f} segundos.')
else:
    print("63.2% da amplitude máxima não foi alcançado.")

plt.show()
