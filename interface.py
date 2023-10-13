import tkinter as tk
from tkinter import ttk

def calcular_pid():
    theta = float(theta_var.get())
    T = float(T_var.get())
    K = float(K_var.get())
    setpoint = float(setpoint_var.get())

    # Cálculo PID do Ziegler-Nichols
    zn_kp = 1.2 * T / (K * theta)
    zn_ki = 2 * theta
    zn_kd = 0.5 * theta

    # Cálculo PID do Cohen-Coon
    cc_kc = ((1 / K) * (T / theta)) * ((4 / 3) + ((1 / 4) * (theta / T)))
    cc_ti = theta * ((32 + (6 * (theta / T))) / (13 + (8 * (theta / T))))
    cc_td = theta * (4 / (11 + 2 * (theta / T)))

    # Limpar a tabela
    for row in resultado_tree.get_children():
        resultado_tree.delete(row)

    # Inserir os resultados na tabela
    resultado_tree.insert('', 'end', values=('PID do ZN', zn_kp, zn_ki, zn_kd))
    resultado_tree.insert('', 'end', values=('PID do Cohen-Coon', cc_kc, cc_ti, cc_td))

root = tk.Tk()
root.title("Configuração do PID")

frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# Crie rótulos e campos de entrada para os parâmetros
labels = ['Theta (θ):', 'T:', 'K:', 'Setpoint:']
entries = []
entry_vars = []

for i, label in enumerate(labels):
    entry_label = tk.Label(frame, text=label)
    entry_label.grid(row=i, column=0)
    entry_var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=entry_var)
    entry.grid(row=i, column=1)
    entries.append(entry)
    entry_vars.append(entry_var)

theta_var, T_var, K_var, setpoint_var = entry_vars

# Botão para calcular
calcular_button = tk.Button(root, text="Calcular", command=calcular_pid)
calcular_button.grid(row=4, column=0)

# Crie uma tabela para exibir os resultados
resultado_tree = ttk.Treeview(root, columns=('1', '2', '3', '4'), show='headings')
resultado_tree.heading('1', text='Método')
resultado_tree.heading('2', text='Kp/Kc')
resultado_tree.heading('3', text='Ki/Ti')
resultado_tree.heading('4', text='Kd/Td')
resultado_tree.grid(row=5, column=0)

root.mainloop()
