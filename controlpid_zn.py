import numpy as np
import control as cnt
import matplotlib.pyplot as plt
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=2.53
tau=6.225
Theta = 1.275 # atraso de propagação
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s
kp=2.89
Ti=2.55
Td=0.6375

print(kp)
print(Ti)
print(Td)
#escrevendo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# Controlador proporcional
numkp = np. array ([kp])
denkp = np. array ([1])
#integral
numki = np. array ([kp])
denki = np. array ([Ti,0])
#derivativo
numkd = np. array ([kp*Td,0])
denkd = np. array ([1])
#Construindo o controlador PID
Hkp = cnt.tf(numkp , denkp)
Hki=cnt.tf(numki , denki)
Hkd=cnt.tf(numkd , denkd)
Hctrl1 = cnt.parallel (Hkp , Hki)
Hctrl = cnt.parallel (Hctrl1 , Hkd)
Hdel = cnt.series (Hs , Hctrl)
#Fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)


t = np . linspace (0 , 35 , 100)
(t , y ) = cnt.step_response ( 15*Hcl, t )
plt.plot (t , y )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Controle PID - ZN')

plt.grid ()
plt.show()