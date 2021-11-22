import matplotlib.pyplot as plt
import networkx as nx
import alkane 
import convert

"""
Example to use `enumerate_isomers` function
"""

# Number of alkane carbon
carbon_count = 7

# Enumerate all possible alkan isomers
isomers = alkane.enumerate_isomers(carbon_count, acyclic=True)

# Visualize
fig, ax = plt.subplots(1, len(isomers), figsize=(3*len(isomers), 3))
for i, isomer in enumerate(isomers):
    nx.draw_kamada_kawai(isomer, ax=ax[i])
plt.savefig(f'C{carbon_count}_isomers.png')

# Convert and export as Gaussian input files
for i, isomer in enumerate(isomers):
    smiles = convert.graph2smiles(isomer)
    convert.smiles2gif(smiles, molname=f"C{carbon_count}_isomer_{i}")
