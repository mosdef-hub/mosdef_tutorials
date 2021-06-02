from glob import glob

import parmed as pmd
import pytest

from foyer import Forcefield

MOL2_FILES = glob('test_molecules/*.mol2')
FORCEFIELD_FILES = glob('*test1.xml')

FORCEFIELD = Forcefield(forcefield_files=FORCEFIELD_FILES)

def atomtype(structure, forcefield, **kwargs):
    """Compare known atomtypes to those generated by foyer.
    Parameters
    ----------
    structure : parmed.Structure
        A parmed structure with `atom.type` attributes.
    forcefield : foyer.Forcefield
        A forcefield to use for atomtyping.
    Raises
    ------
    AssertionError
    """
    known_types = [atom.type for atom in structure.atoms]

    typed_structure = forcefield.apply(structure, **kwargs)

    generated_atom_types = list()
    for i, atom in enumerate(typed_structure.atoms):
        message = (
            "Found multiple or no atom types for atom {} in {}: {}\n"
            "Should be atomtype: {}".format(
                i, structure.title, atom.type, known_types[i]
            )
        )
        assert atom.type, message
        generated_atom_types.append(atom.type)

    both = zip(generated_atom_types, known_types)

    n_types = np.array(range(len(generated_atom_types)))
    known_types = np.array(known_types)
    generated_atom_types = np.array(generated_atom_types)

    non_matches = np.array([a != b for a, b in both])
    message = "Found inconsistent atom types in {}: {}".format(
        structure.title,
        list(
            zip(
                n_types[non_matches],
                generated_atom_types[non_matches],
                known_types[non_matches],
            )
        ),
    )
    assert not non_matches.any(), message

@pytest.mark.parametrize('mol2_file', MOL2_FILES)
def test_atomtyping(mol2_file):
    structure = pmd.load_file(mol2_file, structure=True)
    atomtype(structure, FORCEFIELD)


