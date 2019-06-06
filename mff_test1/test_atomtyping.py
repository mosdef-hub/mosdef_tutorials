from glob import glob

import parmed as pmd
import pytest

from foyer import Forcefield
from foyer.tests.utils import atomtype

MOL2_FILES = glob('test_molecules/*.mol2')
FORCEFIELD_FILES = glob('*.xml')

FORCEFIELD = Forcefield(forcefield_files=FORCEFIELD_FILES)

@pytest.mark.parametrize('mol2_file', MOL2_FILES)
def test_atomtyping(mol2_file):
    structure = pmd.load_file(mol2_file, structure=True)
    atomtype(structure, FORCEFIELD)


