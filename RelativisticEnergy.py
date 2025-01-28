import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Parameter
speed_c = 299792458  # Lichtgeschwindigkeit in m/s
mass_e = 9.1093837139 * 10**-31  # Elektron kg
percentages_coarse = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]  # in percent of c
percentages_fine = np.arange(0.001, 1, 0.001)

def calculateRelativisticEnergy(mass, velocity):
    """Calculate the relativistic energy of an object."""
    return speed_c**2 * mass * (1 / (np.sqrt(1 - velocity**2 / speed_c**2)))

results = [calculateRelativisticEnergy(mass_e, percentage * speed_c) for percentage in percentages_fine]
results_strings = [f"{result:.2e}" for result in results] # deprecated now



# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(percentages_fine, results, color='blue', alpha=0.7)
ax.set_xlabel('v in % of c')
ax.set_ylabel('E_rel in J')
ax.set_title('Relativistic Energy of an Electron')
ax.set_xlim(0, 1)
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))


#table
table_data = [[f"{percentage * 100:.0f}%", f"{calculateRelativisticEnergy(mass_e, percentage * speed_c):.2e}"] for percentage in percentages_coarse]

table = plt.table(cellText=table_data, colLabels=["v in % of c", "E_rel in J"], cellLoc='center', loc='right', bbox=[1.05, 0.1, 0.3, 0.8])
table.auto_set_font_size(False)
table.set_fontsize(10)

plt.tight_layout()
plt.show()