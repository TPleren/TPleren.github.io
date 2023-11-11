import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters voor de perfecte klokkromme
gemiddelde = 100  # Gemiddelde IQ-score
std_afwijking = 15  # Standaardafwijking van IQ-scores

# Creëer een reeks waarden voor de x-as
x = np.linspace(gemiddelde - 4 * std_afwijking, gemiddelde + 4 * std_afwijking, 1000)
# Bereken de PDF (Probability Density Function) van de normale verdeling
pdf = norm.pdf(x, gemiddelde, std_afwijking)

# Teken de klokkromme
plt.plot(x, pdf, color='#72aef8', lw=2, label='Klokkromme')

# Vul het gebied onder de klokkromme binnen één standaardafwijking met een kleur
x_fill_1std = np.linspace(gemiddelde - std_afwijking, gemiddelde + std_afwijking, 1000)
pdf_fill_1std = norm.pdf(x_fill_1std, gemiddelde, std_afwijking)
plt.fill_between(x_fill_1std, pdf_fill_1std, color='#72aef8', alpha=0.3, label='Standaardafwijking 1')

# Vul het gebied onder de klokkromme binnen twee standaardafwijkingen met een andere kleur
x_fill_2std = np.linspace(gemiddelde - 2 * std_afwijking, gemiddelde + 2 * std_afwijking, 1000)
pdf_fill_2std = norm.pdf(x_fill_2std, gemiddelde, std_afwijking)
plt.fill_between(x_fill_2std, pdf_fill_2std, color='orange', alpha=0.3, label='Standaardafwijking 2')

plt.xlabel('IQ-score')
plt.ylabel('Kansdichtheid')
plt.title('Klokkromme van IQ-scores')
plt.legend()
plt.grid(True)
plt.show()
