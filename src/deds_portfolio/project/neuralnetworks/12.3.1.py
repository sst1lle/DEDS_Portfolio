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

# Labels voor output mapping
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
label_map = {i: label for i, label in enumerate(labels)}

# --- Functie om het netwerk te trainen en te evalueren ---
def train_and_evaluate(hidden_size1, hidden_size2, learning_rate, epochs, log_file_path):
    input_size = 25
    output_size = 35

    np.random.seed(42) # Voor reproduceerbaarheid
    
    # Gewichten en biases voor de eerste hidden layer
    weights_input_hidden1 = np.random.randn(input_size, hidden_size1)
    bias_hidden1 = np.random.randn(hidden_size1)
    
    # Gewichten en biases voor de tweede hidden layer
    weights_hidden1_hidden2 = np.random.randn(hidden_size1, hidden_size2)
    bias_hidden2 = np.random.randn(hidden_size2)
    
    # Gewichten en biases voor de output layer
    weights_hidden2_output = np.random.randn(hidden_size2, output_size)
    bias_output = np.random.randn(output_size)

    with open(log_file_path, "w") as log_file:
        log_file.write(f"--- Training gestart: HL1={hidden_size1}, HL2={hidden_size2}, LR={learning_rate}, Epochs={epochs} ---\n")
        print(f"--- Training gestart: HL1={hidden_size1}, HL2={hidden_size2}, LR={learning_rate}, Epochs={epochs} ---")

        for epoch in range(epochs):
            # Feedforward
            hidden1_input = matrix_mul(X, weights_input_hidden1) + bias_hidden1
            hidden1_output = sigmoid(hidden1_input)
            
            hidden2_input = matrix_mul(hidden1_output, weights_hidden1_hidden2) + bias_hidden2
            hidden2_output = sigmoid(hidden2_input)
            
            final_input = matrix_mul(hidden2_output, weights_hidden2_output) + bias_output
            final_output = sigmoid(final_input)

            # Error
            error = y - final_output

            if epoch % 100 == 0:
                mean_abs_error = np.mean(np.abs(error))
                log_message = f"Epoch {epoch}, Error: {mean_abs_error:.8f}\n"
                print(log_message.strip())
                log_file.write(log_message)

            # Backpropagation
            d_output = error * sigmoid_derivative(final_output)
            d_hidden2 = sigmoid_derivative(hidden2_output) * matrix_mul(d_output, weights_hidden2_output.T)
            d_hidden1 = sigmoid_derivative(hidden1_output) * matrix_mul(d_hidden2, weights_hidden1_hidden2.T)

            # Update gewichten
            weights_hidden2_output += matrix_mul(hidden2_output.T, d_output) * learning_rate
            bias_output += np.sum(d_output, axis=0) * learning_rate
            
            weights_hidden1_hidden2 += matrix_mul(hidden1_output.T, d_hidden2) * learning_rate
            bias_hidden2 += np.sum(d_hidden2, axis=0) * learning_rate

            weights_input_hidden1 += matrix_mul(X.T, d_hidden1) * learning_rate
            bias_hidden1 += np.sum(d_hidden1, axis=0) * learning_rate
        
        log_file.write("--- Training voltooid ---\n\n")
        print("--- Training voltooid ---")

        # Evaluatie van training data
        log_file.write("--- Resultaten na training (Originele Data) ---\n")
        print("\n--- Resultaten na training (Originele Data) ---")
        for i in range(len(X)):
            hidden1_input_test = matrix_mul(np.array([X[i]]), weights_input_hidden1) + bias_hidden1
            hidden1_output_test = sigmoid(hidden1_input_test)
            hidden2_input_test = matrix_mul(hidden1_output_test, weights_hidden1_hidden2) + bias_hidden2
            hidden2_output_test = sigmoid(hidden2_input_test)
            final_input_test = matrix_mul(hidden2_output_test, weights_hidden2_output) + bias_output
            final_output_test = sigmoid(final_input_test)

            predicted_label_index = np.argmax(final_output_test)
            predicted_label = label_map[predicted_label_index]
            expected_label_index = np.argmax(y[i])
            expected_label = label_map[expected_label_index]

            result_message = (
                f"\nInput array: {X[i]}\n"
                f"Predicted Output Array: {np.round(final_output_test[0], 2)}\n"
                f"Expected Output Array: {y[i]}\n"
                f"Predicted Label: {predicted_label}\n"
                f"Expected Label: {expected_label}\n"
                f"{'-' * 30}\n"
            )
            print(result_message.strip())
            log_file.write(result_message)

        # --- Extra input data met 20% vervuilde pixels ---
        # Selecteer een paar willekeurige datapunten en knoei ermee
        np.random.seed(42) # Voor reproduceerbaarheid van vervuiling
        
        # Voorbeeld: Neem de eerste 5 datapunten en vervuil ze
        num_corrupt_samples = 5
        X_corrupt = X[:num_corrupt_samples].copy()
        y_corrupt = y[:num_corrupt_samples].copy()

        corruption_percentage = 0.20 # 20% van de pixels
        num_pixels_to_flip = int(input_size * corruption_percentage)

        for i in range(num_corrupt_samples):
            # Kies willekeurige indexen om te flippen
            flip_indices = np.random.choice(input_size, num_pixels_to_flip, replace=False)
            for idx in flip_indices:
                X_corrupt[i, idx] = 1 - X_corrupt[i, idx] # Flip 0 naar 1, of 1 naar 0

        log_file.write("\n--- Resultaten na training (Vervuilde Data) ---\n")
        print("\n--- Resultaten na training (Vervuilde Data) ---")
        for i in range(num_corrupt_samples):
            hidden1_input_test_corrupt = matrix_mul(np.array([X_corrupt[i]]), weights_input_hidden1) + bias_hidden1
            hidden1_output_test_corrupt = sigmoid(hidden1_input_test_corrupt)
            hidden2_input_test_corrupt = matrix_mul(hidden1_output_test_corrupt, weights_hidden1_hidden2) + bias_hidden2
            hidden2_output_test_corrupt = sigmoid(hidden2_input_test_corrupt)
            final_input_test_corrupt = matrix_mul(hidden2_output_test_corrupt, weights_hidden2_output) + bias_output
            final_output_test_corrupt = sigmoid(final_input_test_corrupt)

            predicted_label_index_corrupt = np.argmax(final_output_test_corrupt)
            predicted_label_corrupt = label_map[predicted_label_index_corrupt]
            expected_label_index_corrupt = np.argmax(y_corrupt[i])
            expected_label_corrupt = label_map[expected_label_index_corrupt]

            result_message_corrupt = (
                f"\nOriginal Input: {X[i]}\n"
                f"Corrupted Input ({corruption_percentage*100}% flipped): {X_corrupt[i]}\n"
                f"Predicted Output Array: {np.round(final_output_test_corrupt[0], 2)}\n"
                f"Expected Output Array: {y_corrupt[i]}\n"
                f"Predicted Label: {predicted_label_corrupt}\n"
                f"Expected Label: {expected_label_corrupt}\n"
                f"{'-' * 30}\n"
            )
            print(result_message_corrupt.strip())
            log_file.write(result_message_corrupt)
    
    print(f"\nAlle output is opgeslagen in '{log_file_path}'")


# --- Experimenten uitvoeren ---
# Experiment 1: Baseline met 2 hidden layers (voorbeeld)
print("--- STARTING EXPERIMENT 1 ---")
#train_and_evaluate(hidden_size1=40, hidden_size2=20, learning_rate=0.1, epochs=5000, log_file_path="log_exp1_40_20_5000.txt")

# Experiment 2: Minimaal aantal nodes (voorbeeld, hier moet je zelf mee spelen)
# Begin laag en verhoog geleidelijk totdat correcte voorspellingen worden bereikt
print("\n--- STARTING EXPERIMENT 2 (Minimal Nodes) ---")
# Voorbeeld 1: Zeer weinig nodes
train_and_evaluate(hidden_size1=5, hidden_size2=3, learning_rate=0.1, epochs=5000, log_file_path="12.3.2-test.txt")
# Voorbeeld 2: Iets meer nodes
train_and_evaluate(hidden_size1=10, hidden_size2=5, learning_rate=0.1, epochs=5000, log_file_path="12.3.3-test.txt")
# Voorbeeld 3: Nog meer nodes
train_and_evaluate(hidden_size1=15, hidden_size2=10, learning_rate=0.1, epochs=5000, log_file_path="12.3.4-test.txt")

# Experiment 3: Sterk verhogen/verlagen (voorbeelden)
print("\n--- STARTING EXPERIMENT 3 (Varying Nodes) ---")
# Sterk verhoogd
train_and_evaluate(hidden_size1=100, hidden_size2=80, learning_rate=0.1, epochs=5000, log_file_path="12.3.5-test.txt")
# Sterk verlaagd (kan als onderdeel van Experiment 2)
train_and_evaluate(hidden_size1=5, hidden_size2=3, learning_rate=0.1, epochs=5000, log_file_path="12.3.6-test.txt")