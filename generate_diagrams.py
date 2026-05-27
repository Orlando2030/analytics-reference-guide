import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

# Simulação de dados: Renda vs Filhos
np.random.seed(42)
renda = np.random.normal(5000, 1000, 20)
filhos = np.random.randint(0, 5, 20)

data = np.column_stack((renda, filhos))
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Antes da Padronização
ax1.scatter(renda, filhos, color='red', s=100, alpha=0.6)
ax1.set_title("Antes da Padronização\n(Escala Original)", fontsize=14)
ax1.set_xlabel("Renda (Grande Magnitude)", fontsize=12)
ax1.set_ylabel("Filhos (Pequena Magnitude)", fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)

# Após a Padronização
ax2.scatter(data_scaled[:, 0], data_scaled[:, 1], color='green', s=100, alpha=0.6)
ax2.set_title("Após a Padronização\n(Média 0, Desvio 1)", fontsize=14)
ax2.set_xlabel("Renda (Z-Score)", fontsize=12)
ax2.set_ylabel("Filhos (Z-Score)", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('2_Aprendizado_de_Maquina_e_Modelagem/images/comparativo_padronizacao.png')
print("Diagrama gerado com sucesso em images/comparativo_padronizacao.png")
