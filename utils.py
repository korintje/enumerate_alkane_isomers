from itertools import combinations
import networkx as nx
import grinpy as gp
from pysmiles import write_smiles, fill_valence

MAX_VALENCY = 4

def enumerate_isomers(carbon_count, acyclic=False):
    """ Enumerate all possible saturated alkane from 
        given number of carbons and return as NetworkX Graph object """

    print("Enumerating all possible isomers......")
    randic_indexes = []
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

        # remove hypervalent structures
        is_hypervalent = any([degree[1] > MAX_VALENCY for degree in isomer.degree])
        if is_hypervalent:
            continue
        
        # remove cyclic structures if 'acyclic' is True
        if acyclic and nx.cycle_basis(isomer):
            continue
        
        # remove duplications by wiener index
        randic_index = gp.randic_index(isomer)
        if (randic_index == float('inf')) or (randic_index in randic_indexes):
            continue
        randic_indexes.append(randic_index)

        isomers.append(isomer)

    print("Enumeration finished!")
    return isomers

def graph2smiles(mol):
    for i in range(mol.size()):
        mol.nodes[i]['element'] = 'C'
    fill_valence(mol, respect_hcount=True)
    return write_smiles(mol).replace('[*]', 'C')
