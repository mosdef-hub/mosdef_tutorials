import mbuild as mb
from mbuild.lib.moieties import CH2 
from mbuild.lib.atoms import H


class Alkane(mb.Compound):
    """An alkane chain of a user-defined length."""
    def __init__(self, chain_length):
        """Initialize an Alkane Compound.

        Parameters
        ----------
        chain_length : int
            Length of the alkane chain (in number of carbons)
        """
        # Make sure the user inputs a chain length of at least 1
        if chain_length < 1:
            raise ValueError('Chain length must be greater than 1')

        super(Alkane, self).__init__()

        # Create a polymer of CH2 units
        chain = mb.lib.recipes.Polymer([CH2()])
        chain.build(n = chain_length)
        self.add(chain, 'chain')