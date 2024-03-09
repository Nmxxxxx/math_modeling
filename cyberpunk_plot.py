import matplotlib.pyplot as plt
import pandas
import mplcyberpunk
import numpy as np

categories = ['A', 'B', 'C', 'D']

# Create a DataFrame with 4 columns and 4 rows
data = {
    'Category': categories,
    'Value1': np.random.randint(0, 20, 4),
    'Value2': np.random.randint(0, 20, 4),
    'Value3': np.random.randint(0, 20, 4),
}

df = pandas.DataFrame(data)

with plt.style.context('cyberpunk'):
    df.plot(x='Category', kind='line',
            lw=3, marker='.', ms=20,
            figsize=(10,10))
    mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.4)