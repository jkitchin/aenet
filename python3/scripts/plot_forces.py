#!/usr/bin/env python
"""Plot parity and errors in the energy training.

This relies on the existence of energies.train.0, and energies.test.0
"""
import pandas as pd
import matplotlib.pyplot as plt
from aenet.xsf import read_xsf
from aenet.ase_calculator import ANNCalculator
import numpy as np

train = pd.read_csv('energies.train.0', delim_whitespace=True)
test = pd.read_csv('energies.test.0', delim_whitespace=True)

train_xsf = train['Path-of-input-file']
test_xsf = test['Path-of-input-file']


with open('train.in') as f:
   lines = f.readlines()

lines = [line.strip() for line in lines if line.strip() != '']
lines = [line.strip() for line in lines if not line.startswith('!')]

# Assume the last lines are networks.
i = lines.index('NETWORKS')

potentials = {}

for line in lines[i + 1:]:
   fields = line.split()
   sym = fields[0].strip()
   path = fields[1].strip()
   potentials[sym] = path

calc = ANNCalculator(potentials)

train_known, train_pred = [], []
for xsf in train_xsf:
   atoms = read_xsf(xsf)
   known_f = np.linalg.norm(atoms.get_forces(), axis=1)
   train_known += [known_f]

   atoms.set_calculator(calc)
   pred_f = np.linalg.norm(atoms.get_forces(), axis=1)
   train_pred += [pred_f]

plt.plot(train_known, train_pred, '.', color='DarkBlue')



test_known, test_pred = [], []
for xsf in test_xsf:
   atoms = read_xsf(xsf)
   known_f = np.linalg.norm(atoms.get_forces(), axis=1)
   test_known += [known_f]

   atoms.set_calculator(calc)
   pred_f = np.linalg.norm(atoms.get_forces(), axis=1)
   test_pred += [pred_f]

plt.plot(test_known, test_pred, '.', color='Orange')
plt.show()
