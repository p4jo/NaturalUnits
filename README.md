# NaturalUnits
This provides a calculator for natural units in different bases (preferred: six / 6). Also provides document with lookup and comparison values. 
This is an attempt to make these units usable in any situation (every-day quantities and every scale of science), without sounding strange like "times ten to the thirty kilograms" by using a naming scheme explained below.

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

## Why this system?
Base six is objectively better than any other base due to its factors and size. Ten is not terrible but arbitrary and doesn't handle thirds or sevenths well. Twelve is a lot worse than 6 and so is every other base, especially primes.
Visit https://www.seximal.net/ for jan Misali's plea for using this base.
Also see there for how to say base-six numbers (10 = six, 11 = seven, ..., 20 = twelve, 100 = nif, 10000 = unexian, ...).

Obviously kilo, milli, and powers of those aren't useful in any other base, so it is sensible to use a different system of measurement.

Natural units are those in which the unit quantities are chosen in a way that make frequent conversion factors between physical dimensions disappear (their value in this system is 1) and give us a deeper understanding of the universe as they make dimensions become less and less distinct from one another.

* <img src="https://bit.ly/3gwB3bJ" align="center" border="0" alt="c=1" width="42" height="15" />: Time T and Space L become the same dimension the more you think about the concepts of relativity. Also, energy is momentum in time direction and electric and magnetic fields are part of one field and therefore are also comparable. It is a huge relief of not having to carry around 1/c factors on only one component of a 4D quantity.
* <img src="https://bit.ly/39YpmYJ" align="center" border="0" alt="\hbar =1" width="45" height="15" />: Momentum is related to the change of the wave function: <img src="https://bit.ly/3gwA6QH" align="center" border="0" alt="p^\mu =\pm i\hbar \partial_\mu" width="91" height="19" />. The angular momentum of an atomic electron is quantized in units of <img src="https://bit.ly/39YpmYJ" align="center" border="0" alt="\hbar =1" width="45" height="15" />.
* <img src="https://bit.ly/2Pt023y" align="center" border="0" alt="\frac1{\varepsilon_0}=\mu_0=1" width="78" height="15" />: Electric and magnetic fields equations are clean and fundamental, especially <img src="https://bit.ly/2Xup2vW" align="center" border="0" alt="\nabla \cdot E = \rho" width="80" height="18" />. This defines [partially] rationalized Planck units. Charge becomes a dimensionless quantity, however the elementary charge is only close to 1, not 1.
* <img src="https://bit.ly/39WlIi4" align="center" border="0" alt="\frac1{\varepsilon_0}=\mu_0=2\tau" width="102" height="40" />: Often a <img src="https://bit.ly/3gwC3MJ" align="center" border="0" alt="\frac1{2\tau}" width="21" height="39" /> factor from dilution in three dimensions (area of the 2-sphere) appears together with these constants (energy and force of point charges) and this can be convenient, however this is not fundamental and creates counterintuitive constants in the fundamental equations. This is used in Gaußian cgs-units and standard Planck units. 
* <img src="https://bit.ly/3icKqxz" align="center" border="0" alt="G = 1" width="50" height="15" />: This
takes a similar approach to the Gaußian units.
* <img src="https://bit.ly/2EPBcZz" align="center" border="0" alt="G = \frac1{2\tau}" width="62" height="39" />: This rationalizes the gravitational field as above and simplifies equations in some way related to areas of spheres. Creates Rationalized Planck units, the most fundamental natural units of these.
* <img src="https://bit.ly/3kdzS2V" align="center" border="0" alt="G = \frac1{4\tau}" width="62" height="39" />: This makes the equations of general relativity a bit cleaner.
* <img src="https://bit.ly/2Pt0O0t" align="center" border="0" alt="k_\mathrm B = 1" width="54" height="18" />: Temperature is very much related to energy.

## Names of big and small values
Since the values of 1 in the different dimensions (as listed in the document) are not convenient yet, we need a system like kilo, Mega, Giga, ..., milli, micro, nano, ..., but systematic. I found it compelling to highlight those values that are (multiple of 10)-powers of 10, i.e. powers of <img src="https://bit.ly/3fBAOdP" align="center" border="0" alt="10^{10}" width="33" height="18" />, which only for a relatively small base like six is usable. 
Since - like jan Misali - I like conlangs, especially lojban, the logical language, I thought of naming the exponents (divided by 10) like in lojban: 
* 0 = no, 1 = pa, 2 = re, 3 = ci [ʃi], 4 = vo [vo], 5 = mu, ... (there are named digits up to 23 (hexadecimal))
* Names of numbers are the concatenation of the digits: 10 = pano (alt. xa [xa]), 11 = papa (alt. ze [ze]), 12 = pare (alt. bi), ...
* The number unary minus (as in 'negative 3') is ni'u [nihu], which can - without interference with other words - be shortened to niu (I am not very happy using this one). For example -1254 = ni'u pa ki'o remuvo
* The digit point (not really encouraged to use in this system) is pi. For example τ = 10.141100... = pano pi pavopa panono...
Feel free to suggest different naming schemes in the issues part.

So every power of <img src="https://bit.ly/3fBAOdP" align="center" border="0" alt="10^{10}" width="33" height="18" /> will be assigned the name of the exponent expressed in lojban.
You can therefore call 3 eV a ni'u-pano-Energy or a second a paci-Time. (The dimension is optional, those values were in rationalized Planck units (6-RPU)). 
For more comparison values and SI values refer to the pdf-document in this repository. It was the original goal of this project and produced by python code that generated LaTeX code.
