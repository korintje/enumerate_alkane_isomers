import subprocess
from subprocess import PIPE

def exportgjf(smiles, filename):
    command = f"echo '{smiles}' | obabel -i smi -o gjf --gen3D"
    res = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    with open(filename, "w") as f:
        f.write(res.stdout)
    