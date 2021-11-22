import subprocess
from subprocess import PIPE
from pysmiles import write_smiles, fill_valence

"""
Caution: Very adhoc and limited-use functions
"""

def graph2smiles(mol):
    for i in range(mol.size()):
        mol.nodes[i]['element'] = 'C'
    fill_valence(mol, respect_hcount=True)
    return write_smiles(mol).replace('[*]', 'C')

def smiles2gif(smiles, molname, fb="b3lyp/6-31g(d,p)"):
    cmd = f"echo '{smiles}' | obabel -i smi -o gjf --gen3D"
    res = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    texts = res.stdout.split("\n")
    texts[0] = r"%chk=" + f"{molname}.chk"
    texts[1] = f"#p {fb} opt freq"
    texts[3] = molname
    with open(f"{molname}.gjf", "w") as f:
        f.write("\n".join(texts))