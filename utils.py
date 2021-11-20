from itertools import combinations
import networkx as nx

MAX_VALENCY = 4

def enumerate_isomers(carbon_count, acyclic=False):
    """ Enumerate all possible saturated alkane from 
        given number of carbons and return as NetworkX Graph object """

    print("Enumerating all possible isomers......")
    wiener_indexes = []
    isomers = []

    # enumerate all possible bonding combinations of numeically labeled carbons 
    bond_count = carbon_count - 1
    bonds = list(combinations(range(carbon_count), 2))
    bond_combinations = list(combinations(bonds, bond_count))

    for bond_combination in bond_combinations:

        # Create "isomer" as a non-directed graph
        isomer = nx.Graph()
        for bond in bond_combination:
            isomer.add_edge(*bond)
        
        # remove duplications by wiener index
        wiener_index = nx.algorithms.wiener.wiener_index(isomer)
        if (wiener_index == float('inf')) or (wiener_index in wiener_indexes):
            continue
        wiener_indexes.append(wiener_index)

        # remove hypervalent structures
        is_hypervalent = any([degree[1] > MAX_VALENCY for degree in isomer.degree])
        if is_hypervalent:
            continue
        
        # remove cyclic structures if 'acyclic' is True
        if acyclic and nx.cycle_basis(isomer):
            continue
        
        isomers.append(isomer)

    print("Enumeration finished!")
    return isomers
