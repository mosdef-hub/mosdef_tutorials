# MoSDeF: A Molecular Simulation and Design Framework
MoSDeF consists of a collection of Python packages aimed at simplifying the
creation, atom-typing, and simulation of complex molecular models - with a particular
focus on the use of programmatic routines that allow for screening over large
structural parameter spaces and the encapsulation of these routines to
facilitate reproducibility.

MoSDeF is founded around two core Python packages:

* [mBuild](https://github.com/mosdef-hub/mbuild): A hierarchical, component-based
molecule builder
* [Foyer](https://github.com/mosdef-hub/foyer): A package for atom-typing as well as applying and disseminating forcefields

## Installation

To access the MoSDeF tutorials clone this repository using:

```
git clone --recurse-submodules https://github.com/mosdef-hub/mosdef_tutorials.git
```

Note the addition of the `--recurse-submodules` flag to the standard `git clone` command.
The mBuild and Foyer tutorials are included here as submodules and this flag
is necessary to download them.

## Tutorials
This repository features a collection of tutorials and examples to help new users get
familiarized with the MoSDeF toolkit. These tutorials/examples are organzied as
follows:

### [mBuild](https://github.com/mosdef-hub/mosdef_tutorials/mbuild_tutorials)

* mBuild 00: Getting Started
* mBuild 01: Basic Functionality
* mBuild 02: Resuing Components
* mBuild 03: Connecting Components with Ports
* mBuild 04: Constructing Larger Compounds
* mBuild 05: Creating Flexible Classes
* mBuild 06: Setting Up Bulk Systems
* mBuild 07: Energy Minimization
* mBuild 08: Building Polymers
* mBuild 09: Surface Functionalization

The mBuild tutorials can also be accessed through the [mBuild tutorials repository](https://github.com/mosdef-hub/mbuild_tutorials).

### [Foyer](https://github.com/mosdef-hub/mosdef_tutorials/foyer-tutorials)

* Foyer 00: Getting Started
* Foyer 01: SMARTS and Overrides
* Foyer 02: SMARTS for Non-Atomistic Systems
* Foyer 03: Creating Force Field Files

The Foyer tutorials can also be accessed through the [Foyer tutorials repository](https://github.com/mosdef-hub/foyer_tutorials).

A series of full examples demonstrating how systems constructed with mBuild
and Foyer can be used for performing simulations are currently under
construction.

You can access this repository and run these tutorials interactively in-browser
through our Binder link:
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mosdef-hub/mosdef_tutorials/master)

If you would like a more general introduction to these tools, we have also
included an "Overview" notebook that can be accessed through the following
Binder link:
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mosdef-hub/mosdef_tutorials/master?filepath=overview.ipynb)

Additionally, if you would like to access only the mBuild or only the Foyer tutorials,
these can be accessed through the following Binder links:

__mBuild__ [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mosdef-hub/mbuild_tutorials/master)

__Foyer__ [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mosdef-hub/foyer_tutorials/master)
