import matplotlib.pyplot as plt
import numpy as np

# Daten
V = np.array([5.0, 10, 15, 17.5, 20, 22.5, 25, 30, 35], dtype=float)
pH = np.array([4.3, 4.7, 5.2, 5.5, 6.1, 11.5, 11.9, 12.2, 12.3], dtype=float)

# Mittlere Steigung für jeden Streckenabschnitt der Kurve berechnen:
def dSteigung(lineXarr=V, lineYarr=pH):
    dS = []
    for i in range(len(lineXarr) - 1):  # Use len(lineXarr) - 1 to avoid index out of range
        dS.append((lineYarr[i + 1] - lineYarr[i]) / (lineXarr[i + 1] - lineXarr[i]))
    return dS

# Lineare Interpolation Funktion; gibt y für x wert zwischen punkten x_i und x_i+1 zurück
# meine eigene schlechte version von np.interp() :D
def linInterp(x , x_arr, y_arr):
    for i in range(len(x_arr) - 1):
        if x_arr[i] <= x <= x_arr[i + 1]:
            return y_arr[i] + dSteigung(x_arr[i:i+2], y_arr[i:i+2])[0] * (x - x_arr[i])
    raise ValueError("x liegt außerhalb des Bereichs")


# Äquivalenzpunkt bei maximaler Steigung
dpH_dV = dSteigung(V,pH)
idx_eq = dpH_dV.index(max(dpH_dV))# index größten Anstiegs # could fail when rounding?
#V_eq = V[idx_eq] # Volumen am ÄP
V_eq = (V[idx_eq] + V[idx_eq+1])/2 # Volumen am ÄP; Mittel aus Strecke (def. 2 Pkt!)

# Steigung für lineare Funktion zwischen Punkten der größten Steigung (m)
m = dpH_dV[idx_eq]

# Lineare interpolation um exakten pH at V_eq zu finden (punkt liegt auf mitte der gerade zwischen idx und idx+1
pH_eq = m * (V_eq - V[idx_eq]) + pH[idx_eq]





# Anfangskonzentration Essigsäure
c_base = 0.10 # mol/L
V_acid = 30e-3 # 30 mL = 0.03 L
c_acid = c_base * (V_eq / 1000) / V_acid

# pKs
V_half = V_eq / 2 # Halbäquivalenzpunkt
pH_half = linInterp(V_half, V, pH)
pKs = pH_half # pH = pKs bei Halb-ÄP

# Plot Titrationskurve
plt.figure()
plt.plot(V, pH, marker='o')
plt.xlabel("Zugabe NaOH (mL)")
plt.ylabel("pH")
plt.title("Titrationskurve Essigsäure + NaOH")
plt.hlines(pH_eq, min(V), max(V), colors='r', linestyles='dashed', label='Äquivalenzpunkt')
plt.vlines(V_eq, min(pH), max(pH), colors='r', linestyles='dashed')
plt.hlines(pKs, min(V), max(V), colors='b', linestyles='dotted', label='pH=pKs')
plt.vlines(V_half, min(pH), max(pH), colors='b', linestyles='dotted', label='Halb-Äquivalenzpunkt')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Konzentration Essigsäure =", c_acid, "mol/L")
print("pKs =", pKs)
print("Äquivalenzpunkt bei", V_eq, "mL")
print("pH bei Äquivalenzpunkt =", pH_eq)


"""import matplotlib.pyplot as plt

# Vol
x = [0.0, 1.0, 2.0, 3.0, 4.0]
# pH
y = [2.1, 2.3, 2.9, 5.8, 7.1]


plt.figure()
plt.plot(x, y, marker='o')
plt.title("Titrationskurve")
plt.xlabel("Volumen (mL)")
plt.ylabel("pH")
plt.grid(True)
plt.tight_layout()
plt.show()

"""



