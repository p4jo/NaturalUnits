# NaturalUnits
This provides a calculator for natural units (preferred: ε<sub>0</sub> = 1, G = 1) in different bases (preferred: six / 6), with different naming schemes (preferred: DividedByBaseInLojbanNumbering, od DividedByBaseAndItalic). Also provides document with lookup and comparison values.

## Usage:
Enter number or expression like the following. `value;Dimension` converts from SI to natural units, `value:Dimension` from natural units to SI. Dimensions are written additively.
* `14E-3;M+L-T`
* `=J/C`
* `=#/s`
* `55;E*2-Θ + # -31.4E22 *2E3`

Enter python code à la:

* `inputBase=10`
* `base=7` (output base)
* Change the System of natural units: `eps0_is_1 = False` or: `G_is_1 = False` and afterwards: `SetupSystem()`

Enter commands like:
* `SetExpRule` / `setExp rule` ...
* `set name of exponents` / `SetName of exponents` ...
* `exit`

Make (partial) LaTeX document: `CreateSmallDocument()`. 
Or `CreateDocument(complicated parameters - look at the code)` or change the parameters at the top of the python script (e.g. in the command line) and run `CreateBigDocument()`

## Versions:
There is a hosted version:
https://NaturalUnits.thebytebreaker.repl.run

Created documents can be downloaded from the links provided there by using `get tex files` or `get pdf`

You can also clone this repo.

## Why and why those names of exponents?
Base six is objectively better than any other base due to its factors and size. Ten is not terrible but arbitrary and doesn't handle thirds or sevenths well. Twelve is a lot worse than 6 and so is every other base, especially primes.
Visit https://www.seximal.net/ for jan Misali's plea for using this base.

Obviously kilo, milli, and powers of those aren't useful in any other base, so it is sensible to use a different system of measurement.

Natural units are those in which the unit quantities are chosen in a way that make frequent conversion factors between physical dimensions disappear (by having _value_ 1) and give us a deeper understanding of the universe as they make dimensions become less and less distinct from one another:
* <img src="https://bit.ly/3gwB3bJ" align="center" border="0" alt="c=1" width="42" height="15" />: Time T and Space become the same dimension the more you think about space-time (Relativity). This means velocity is expressed in units of c. Also energy is momentum in time direction; electric and magnetic fields are part of one field. 
* <img src="https://bit.ly/39YpmYJ" align="center" border="0" alt="\hbar =1" width="45" height="15" />: Momentum is related to the change of the wave function: <img src="https://bit.ly/3gwA6QH" align="center" border="0" alt="p^\mu =\pm i\hbar \partial_\mu" width="72" height="15" />
* <img src="https://bit.ly/3fxioej" align="center" border="0" alt="\varepsilon_0=\mu_0=1" width="78" height="15" />: Electric and magnetic fields equations are simple and clean, no thought required.
<img src="https://bit.ly/2XxthXl" align="center" border="0" alt="\frac1{\varepsilon_0}=\mu_0=2\tau" width="102" height="40" />