import numpy as np

# Activatiefunctie (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Afgeleide van sigmoid voor backprop
def sigmoid_derivative(x):
    return x * (1 - x)

# Matrixvermenigvuldiging zonder np.dot
def matrix_mul(a, b):
    result = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                result[i][j] += a[i][k] * b[k][j]
    return result

# --- Dataset voor 5x5 pixels (met 2-3 varianten per label) ---
# Input: 5x5 pixelwaarden (0 of 1), voorgesteld als 25-element arrays
# Dit zijn zelfgemaakte voorbeelddata
X = np.array([
    # Nummers 1 t/m 9
    # 1
    [0,0,1,0,0, 
     0,1,1,0,0, 
     0,0,1,0,0, 
     0,0,1,0,0, 
     0,1,1,1,0], # 1_var1

    [0,1,0,0,0, 
     0,1,0,0,0, 
     0,1,0,0,0, 
     0,1,0,0,0, 
     0,1,1,1,0], # 1_var2
     
    # 2
    [0,1,1,1,0, 1,0,0,0,1, 0,0,1,1,0, 0,1,0,0,0, 1,1,1,1,1], # 2_var1
    [0,1,1,1,0, 1,0,0,0,1, 0,0,1,0,0, 0,1,0,0,0, 1,1,1,1,1], # 2_var2
    [0,1,1,1,0, 0,0,0,0,1, 0,0,1,1,0, 0,1,0,0,0, 1,1,1,1,1], # 2_var3
    # 3
    [0,1,1,1,0, 1,0,0,0,1, 0,0,1,1,0, 1,0,0,0,1, 0,1,1,1,0], # 3_var1
    [0,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0], # 3_var2
    # 4
    [0,0,1,0,0, 0,1,1,0,0, 1,0,1,0,0, 1,1,1,1,1, 0,0,1,0,0], # 4_var1
    [1,0,0,0,0, 1,0,1,0,0, 1,1,1,1,0, 0,0,1,0,0, 0,0,1,0,0], # 4_var2
    # 5
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,0, 0,0,0,0,1, 1,1,1,1,0], # 5_var1
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0], # 5_var2
    # 6
    [0,1,1,1,0, 1,0,0,0,0, 1,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0], # 6_var1
    [0,0,1,1,0, 0,1,0,0,0, 0,1,1,1,0, 0,1,0,0,1, 0,0,1,1,0], # 6_var2
    # 7
    [1,1,1,1,1, 0,0,0,0,1, 0,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0], # 7_var1
    [1,1,1,1,1, 0,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0, 1,0,0,0,0], # 7_var2
    # 8
    [0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0], # 8_var1
    [0,1,1,1,0, 1,0,1,0,1, 0,1,1,1,0, 1,0,1,0,1, 0,1,1,1,0], # 8_var2
    # 9
    [0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,1, 0,0,0,0,1, 0,1,1,1,0], # 9_var1
    [0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0, 0,0,0,1,0, 0,1,1,0,0], # 9_var2

    # Letters A t/m Z (voorbeeld, niet alle letters hebben 3 varianten i.v.m. omvang)
    # A
    [0,1,1,1,0, 1,0,0,0,1, 1,1,1,1,1, 1,0,0,0,1, 1,0,0,0,1], # A_var1
    [0,1,1,1,0, 1,0,1,0,1, 1,1,1,1,1, 1,0,1,0,1, 1,0,1,0,1], # A_var2
    # B
    [1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0], # B_var1
    [1,1,1,0,0, 1,0,0,1,0, 1,1,1,0,0, 1,0,0,1,0, 1,1,1,0,0], # B_var2
    # C
    [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,0, 1,0,0,0,1, 0,1,1,1,0], # C_var1
    [0,1,1,1,1, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 0,1,1,1,1], # C_var2
    # D
    [1,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 1,1,1,1,0], # D_var1
    [1,1,1,0,0, 1,0,0,1,0, 1,0,0,1,0, 1,0,0,1,0, 1,1,1,0,0], # D_var2
    # E
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,0, 1,0,0,0,0, 1,1,1,1,1], # E_var1
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,0,0, 1,0,0,0,0, 1,1,1,1,1], # E_var2
    # F
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,0, 1,0,0,0,0, 1,0,0,0,0], # F_var1
    [1,1,1,1,1, 1,0,0,0,0, 1,1,1,0,0, 1,0,0,0,0, 1,0,0,0,0], # F_var2
    # G
    [0,1,1,1,0, 1,0,0,0,1, 1,0,1,1,1, 1,0,0,0,1, 0,1,1,1,0], # G_var1
    [0,1,1,1,0, 1,0,0,0,0, 1,0,1,1,0, 1,0,0,0,1, 0,1,1,1,0], # G_var2
    # H
    [1,0,0,0,1, 1,0,0,0,1, 1,1,1,1,1, 1,0,0,0,1, 1,0,0,0,1], # H_var1
    [1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1], # H_var2
    # I
    [1,1,1,1,1, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 1,1,1,1,1], # I_var1
    [0,1,1,1,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,1,1,1,0], # I_var2
    # J
    [0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0], # J_var1
    [0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 1,0,0,1,0, 0,1,1,0,0], # J_var2
    # K
    [1,0,0,0,1, 1,0,0,1,0, 1,1,1,0,0, 1,0,0,1,0, 1,0,0,0,1], # K_var1
    [1,0,0,0,1, 1,0,1,0,0, 1,1,0,0,0, 1,0,1,0,0, 1,0,0,0,1], # K_var2
    # L
    [1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,1,1,1,1], # L_var1
    [1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 0,1,1,1,1], # L_var2
    # M
    [1,0,0,0,1, 1,1,0,1,1, 1,0,1,0,1, 1,0,0,0,1, 1,0,0,0,1], # M_var1
    [1,0,0,0,1, 1,1,0,1,1, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1], # M_var2
    # N
    [1,0,0,0,1, 1,1,0,0,1, 1,0,1,0,1, 1,0,0,1,1, 1,0,0,0,1], # N_var1
    [1,0,0,0,1, 1,1,0,0,1, 1,0,0,1,1, 1,0,0,0,1, 1,0,0,0,1], # N_var2
    # O
    [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0], # O_var1
    [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0], # O_var2
    # P
    [1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0, 1,0,0,0,0, 1,0,0,0,0], # P_var1
    [1,1,1,1,0, 1,0,0,0,1, 1,1,1,0,0, 1,0,0,0,0, 1,0,0,0,0], # P_var2
    # Q
    [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,1,0, 0,1,1,0,1], # Q_var1
    [0,1,1,1,0, 1,0,0,0,1, 1,0,1,0,1, 1,0,0,1,0, 0,1,1,0,1], # Q_var2
    # R
    [1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0, 1,0,0,1,0, 1,0,0,0,1], # R_var1
    [1,1,1,1,0, 1,0,0,0,1, 1,1,1,0,0, 1,0,0,1,0, 1,0,0,0,1], # R_var2
    # S
    [0,1,1,1,1, 1,0,0,0,0, 0,1,1,1,0, 0,0,0,0,1, 1,1,1,1,0], # S_var1
    [1,1,1,1,0, 1,0,0,0,0, 0,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0], # S_var2
    # T
    [1,1,1,1,1, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0], # T_var1
    [1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0], # T_var2
    # U
    [1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0], # U_var1
    [1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,1], # U_var2
    # V
    [1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,0,1,0, 0,0,1,0,0], # V_var1
    [1,0,0,0,1, 1,0,0,0,1, 0,1,0,1,0, 0,1,0,1,0, 0,0,1,0,0], # V_var2
    # W
    [1,0,0,0,1, 1,0,0,0,1, 1,0,1,0,1, 1,1,0,1,1, 0,1,1,1,0], # W_var1
    [1,0,0,0,1, 1,0,0,0,1, 1,0,1,0,1, 1,0,1,0,1, 0,1,0,1,0], # W_var2
    # X
    [1,0,0,0,1, 0,1,0,1,0, 0,0,1,0,0, 0,1,0,1,0, 1,0,0,0,1], # X_var1
    [1,0,0,0,1, 0,1,0,1,0, 1,0,1,0,1, 0,1,0,1,0, 1,0,0,0,1], # X_var2
    # Y
    [1,0,0,0,1, 0,1,0,1,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0], # Y_var1
    [1,0,0,0,1, 0,1,0,1,0, 0,1,1,1,0, 0,0,1,0,0, 0,0,1,0,0], # Y_var2
    # Z
    [1,1,1,1,1, 0,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0, 1,1,1,1,1], # Z_var1
    [1,1,1,1,1, 0,0,0,0,1, 0,0,0,1,0, 0,0,1,0,0, 1,1,1,1,1], # Z_var2
])

# Labels voor elk patroon (1 output node per label)
# Nummers 1 t/m 9, dan A t/m Z (in volgorde van de X-array)
# Totaal 9 + 26 = 35 unieke labels
y = np.array([
    # Nummers (1-9)
    [1,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 1_var1
    [1,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 1_var2

    [0,1,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 2_var1
    [0,1,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 2_var2
    [0,1,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 2_var3

    [0,0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 3_var1
    [0,0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 3_var2

    [0,0,0,1,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 4_var1
    [0,0,0,1,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 4_var2

    [0,0,0,0,1,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 5_var1
    [0,0,0,0,1,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 5_var2

    [0,0,0,0,0,1,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 6_var1
    [0,0,0,0,0,1,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 6_var2

    [0,0,0,0,0,0,1,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 7_var1
    [0,0,0,0,0,0,1,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 7_var2

    [0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 8_var1
    [0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 8_var2

    [0,0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 9_var1
    [0,0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # 9_var2

    # Letters (A-Z)
    [0,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # A_var1
    [0,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # A_var2

    [0,0,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # B_var1
    [0,0,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # B_var2

    [0,0,0,0,0,0,0,0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # C_var1
    [0,0,0,0,0,0,0,0,0, 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # C_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # D_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # D_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # E_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # E_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # F_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # F_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # G_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # G_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # H_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # H_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # I_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # I_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # J_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # J_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # K_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # K_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # L_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # L_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], # M_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], # M_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], # N_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], # N_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # O_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # O_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], # P_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], # P_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], # Q_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], # Q_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # R_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # R_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], # S_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], # S_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], # T_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], # T_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], # U_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], # U_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], # V_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], # V_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], # W_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], # W_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], # X_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], # X_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], # Y_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], # Y_var2

    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], # Z_var1
    [0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], # Z_var2
])

# Netwerk parameters
input_size = 25  # 5x5 pixels
hidden_size = 80 # Aangepast voor meer complexiteit
output_size = 35 # 9 cijfers + 26 letters
learning_rate = 0.1 # Aangepast learning rate
epochs = 1000 # Meer epochs voor betere training

# Initialisatie
np.random.seed(42)
weights_input_hidden = np.random.randn(input_size, hidden_size)
bias_hidden = np.random.randn(hidden_size)
weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_output = np.random.randn(output_size)

# Mapping van output index naar label
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
label_map = {i: label for i, label in enumerate(labels)}

print("Test 3e training afbeelding")
print("--- Training gestart ---")
# Training
for epoch in range(epochs):
    # Feedforward
    hidden_input = matrix_mul(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)
    final_input = matrix_mul(hidden_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_input)

    # Error
    error = y - final_output

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Error: {np.mean(np.abs(error)):.8f}") # Verhoog precisie error

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = sigmoid_derivative(hidden_output) * matrix_mul(d_output, weights_hidden_output.T)

    # Update gewichten
    weights_hidden_output += matrix_mul(hidden_output.T, d_output) * learning_rate
    bias_output += np.sum(d_output, axis=0) * learning_rate
    weights_input_hidden += matrix_mul(X.T, d_hidden) * learning_rate
    bias_hidden += np.sum(d_hidden, axis=0) * learning_rate

print("--- Training voltooid ---")

print("\n--- Resultaten na training ---")
for i in range(len(X)):
    # Feedforward voor specifieke input
    hidden_input_test = matrix_mul(np.array([X[i]]), weights_input_hidden) + bias_hidden
    hidden_output_test = sigmoid(hidden_input_test)
    final_input_test = matrix_mul(hidden_output_test, weights_hidden_output) + bias_output
    final_output_test = sigmoid(final_input_test)

    predicted_label_index = np.argmax(final_output_test)
    predicted_label = label_map[predicted_label_index]
    expected_label_index = np.argmax(y[i])
    expected_label = label_map[expected_label_index]

    print(f"\nInput array: {X[i]}")
    print(f"Predicted Output Array: {np.round(final_output_test[0], 2)}")
    print(f"Expected Output Array: {y[i]}")
    print(f"Predicted Label: {predicted_label}")
    print(f"Expected Label: {expected_label}")
    print("-" * 30)