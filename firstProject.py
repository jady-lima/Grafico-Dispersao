import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = {'x': np.random.rand(50), 'y': np.random.rand(50)}

df = pd.DataFrame(data)

sns.scatterplot(x='x', y='y', data=df)

plt.show()
