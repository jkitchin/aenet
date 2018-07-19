#!/usr/bin/env python
"""Plot convergence of RMSE/MAE with training.
The data is written to 'train-convergence.csv'

You can run this any time you want in a training directory.

"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train-convergence.csv', sep=",")

plt.subplot(1, 2, 1)
plt.plot(df['epoch'], df['train-<RMSE>'])
plt.plot(df['epoch'], df['test-<RMSE>'])
plt.title('<RMSE> convergence')
plt.xlabel('Epoch')
plt.ylabel('<RMSE> (eV/atom)')
plt.legend(['train', 'test'])

plt.subplot(1, 2, 2)
plt.plot(df['epoch'], df['train-MAE'])
plt.plot(df['epoch'], df['test-MAE'])
plt.title('MAE convergence')
plt.xlabel('Epoch')
plt.ylabel('MAE (eV/atom)')
plt.legend(['train', 'test'])

plt.tight_layout()
plt.show()
