from collections import Counter 
from itertools import combinations, chain
import networkx as nx
import matplotlib.pyplot as plt

def enumerate_isomers(carbon_count):
    """ Generate all possible saturated and acyclic alkane
        structures from given number of carbons, and return
        as NetworkX Graph object """

    wiener_indexes = []
    isomers = []

    # enumerate all possible bonding combinations of numeically labeled carbons 
    print("Enumerating possible bond combinations......")
    bond_count = carbon_count - 1
    bonds = list(combinations(range(carbon_count), 2))
    bond_combinations = list(combinations(bonds, bond_count))

    # Remove inappropriate structures
    print("Removing inappropriate structures...... (may take a long time)")
    for bond_combination in bond_combinations[:]:
        flattened = list(chain.from_iterable(bond_combination))
        used_id_count = len(set(flattened))
        carbon_valences = Counter(flattened).values()
        # Remove cyclic structures
        if used_id_count < carbon_count:
            bond_combinations.remove(bond_combination)
        # Remove hypervalent structures
        elif any([valence > 4 for valence in carbon_valences]):
            bond_combinations.remove(bond_combination)

    # Convert to NetworkX graph object and remove duplication by wiener index
    print("Removing duplications by Wiener index......")
    for bond_combination in bond_combinations:
        isomer = nx.Graph()
        for bond in bond_combination:
            isomer.add_edge(*bond)
        wiener_index = nx.algorithms.wiener.wiener_index(isomer)
        if (wiener_index != float('inf')) and (not wiener_index in wiener_indexes):
            wiener_indexes.append(wiener_index)
            isomers.append(isomer)
    
    print("Enumeration finished!")
    return isomers


if __name__ == '__main__':
    print("Start script")
    carbon_count = 7
    isomers = enumerate_isomers(carbon_count)
    fig, ax = plt.subplots(1, len(isomers), figsize=(3*len(isomers), 3))
    for i, isomer in enumerate(isomers):
        nx.draw_kamada_kawai(isomer, ax=ax[i])
    plt.savefig(f'C{carbon_count}_isomers.png')




