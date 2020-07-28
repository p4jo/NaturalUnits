# NaturalUnits
This provides a calculator for natural units (preferred: eps0 = 1, G = 1) in different bases (preferred: 6), with different naming schemes (preferred: DividedByBaseInLojbanNumbering). Also provides LaTeX document with lookup and comparison values.

## Usage:
Enter number or expression like the following. value;Dimension converts from SI to nat. units, value:Dimension from nat.Units to SI.
* 14E-3;M+L-T
* =J/C
* =#/s

Enter python code à la:

* inputBase=10
* base=7 (output base)
* Change the System of natural units: eps0_is_1 = False or: G_is_1 = False and afterwards: SetupSystem()
* Make (partial) LaTeX document: CreateDocument(). Please change the parameters at the top of the python script (e.g. in the command line), or else it will take a long time and create the same document I provided

Enter commands like:
* SetExpRule
* exit
