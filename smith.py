import numpy as np
import control as cnt
import matplotlib.pyplot as plt
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=2.533
tau=19.89
Theta = 4.06 # atraso de propagação

degrau = 15


num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)
#Hmf = cnt.feedback(Hs, 1)

t = np . linspace (0, 35, 100)
(t , y ) = cnt.step_response ( Hs, t )
#(t, y1) = cnt.step_response(Hmf, t)
plt.plot (t , y )
#plt.plot(t, y1)
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('smith')

plt.grid ()
plt.show()