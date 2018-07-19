#!/usr/bin/env python
"""Plot parity and errors in the energy training.

This relies on the existence of energies.train.0, and energies.test.0
"""
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv('energies.train.0', delim_whitespace=True)
test = pd.read_csv('energies.test.0', delim_whitespace=True)

train_err = (train['Ref(eV)'] - train['ANN(eV)']) / train['#atoms']
test_err = (test['Ref(eV)'] - test['ANN(eV)']) / test['#atoms']

plt.subplot(3, 1, 1)
plt.plot(train['Ref(eV)'], train['ANN(eV)'], marker='.', color='DarkBlue')
plt.plot(test['Ref(eV)'], test['ANN(eV)'], marker='.', color='Orange')
plt.legend(['train', 'test'])
plt.xlabel('Energy (eV)')
plt.ylabel('ANN (eV)')

plt.subplot(3, 1, 2)
plt.hist(train_err)
plt.hist(test_err)
plt.xlabel('ΔE (eV/atom)')
#plt.title(f"MAE train: {train_err.abs().mean():1.3f} Std: {train_err.std():1.3f}"
#          f"\nMAE train: {test_err.abs().mean():1.3f} Std: {test_err.std():1.3f}")
plt.legend(['train', 'test'])


plt.subplot(3, 1, 3)
plt.plot(train['Ref(eV)'], train_err, marker='.',
         linestyle='', color='DarkBlue')
plt.plot(test['Ref(eV)'], test_err, marker='.',
         linestyle='', color='Orange')

test_mae = test_err.abs().mean()
plt.text(x=test['Ref(eV)'].mean(), y=test_mae, s=f'MAE = {test_mae:1.4f}')
plt.axhline(y=test_mae, linestyle='--', color='k')
plt.legend(['train', 'test'])
plt.xlabel('Energy (eV)')
plt.ylabel('Error')
plt.tight_layout()
plt.show()
