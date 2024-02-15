import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerar dados aleatórios
np.random.seed(42)
data = {'x': np.random.rand(50), 'y': np.random.rand(50)}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Plotar um gráfico de dispersão usando Seaborn
sns.scatterplot(x='x', y='y', data=df)

# Mostrar o gráfico
plt.show()
