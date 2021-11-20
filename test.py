import matplotlib.pyplot as plt
import networkx as nx
import utils 

carbon_count = 7
isomers = utils.enumerate_isomers(carbon_count, acyclic=True)
fig, ax = plt.subplots(1, len(isomers), figsize=(3*len(isomers), 3))
for i, isomer in enumerate(isomers):
    nx.draw_kamada_kawai(isomer, ax=ax[i])
plt.savefig(f'C{carbon_count}_isomers.png')

for i, isomer in enumerate(isomers):
    print("size: ", isomer.size())
    smiles = utils.graph2smiles(isomer)
    utils.write_gjf_from_smiles(smiles, f"C{carbon_count}isomer{i}.gjf") 