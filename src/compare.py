import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos CSV
edmonds_data = pd.read_csv('edmondsLog.csv')
spaghetti_data = pd.read_csv('spaghettiLog.csv')

# Gerar gráficos comparativos
plt.figure(figsize=(5,5))

# Gráfico para tempo de execução
plt.hist(edmonds_data['time'], bins=20, alpha=0.5, label='Edmonds')
plt.hist(spaghetti_data['time'], bins=20, alpha=0.5, label='Spaghetti')
plt.xlabel('Tempo de Execução')
plt.ylabel('Frequência')
plt.title('Comparação do Tempo de Execução')
plt.legend()


plt.tight_layout()
plt.show()

