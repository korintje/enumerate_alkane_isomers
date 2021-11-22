# enumerate_alkane_isomers
Enumerate all saturated and acyclic alkane isomers for a given number of carbons

![C7_isomers](https://user-images.githubusercontent.com/30950088/142826482-052eb3ad-e974-4318-97da-b9749657f2ea.png)

## dependencies
### for isomer enumeration
- [networkx](https://networkx.org/)
- [grinpy](https://pypi.org/project/grinpy/)
- [scipy](https://scipy.org/)
### for gjf conversion
- [openbabel](http://openbabel.org/wiki/Main_Page)
- [pysmiles](https://github.com/pckroon/pysmiles)
### for visualization
- [matplotlib](https://matplotlib.org/)

## Setup
- e.g. on Ubuntu
```
pip install networkx grinpy scipy pysmiles matplotlib
sudo apt update && install openbabel -y
```

## Usage
modify parameter "N" in `test.py` and
```
python test.py
```
