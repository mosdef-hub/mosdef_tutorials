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
        chain = mb.Polymer(CH2(), n=chain_length, port_labels=('up', 'down'))
        self.add(chain, 'chain')

        # Cap one end of the polymer with a hydrogen
        self.add(H(), 'up_cap')
        mb.force_overlap(move_this=self['up_cap'],
                         from_positions=self['up_cap']['up'],
                         to_positions=self['chain']['up'])

        # Cap the other end of the polymer with a hydrogen
        self.add(H(), 'down_cap')
        mb.force_overlap(move_this=self['down_cap'],
                         from_positions=self['down_cap']['up'],
                         to_positions=self['chain']['down'])
