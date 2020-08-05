# NaturalUnits
Provides a calculator for natural units and programmatically generated documents with lookup and comparison values expressed in these units. 
This is an attempt to make natural units usable in any situation (every-day quantities and every scale of science) by using a naming scheme explained below, and at the same time creating a system of units for base 6.

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
Or `CreateDocument(complicated parameters)` or change the parameters at the top of the python script (e.g. in the command line) and run `CreateBigDocument()`

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

* <img src="http://chart.apis.google.com/chart?cht=tx&chl=c%3D1&chf=bg%2Cs%2CFFFFFF80&chco=000000&chs=20">: Time T and Space L become the same dimension the more you think about the concepts of relativity. Also, energy is momentum in time direction and electric and magnetic fields are part of one field and therefore are also comparable. It is a huge relief of not having to carry around 1/c factors on only one component of a 4D quantity.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Chbar%20%3D%201&chf=bg%2Cs%2CFFFFFF80&chco=000000&chs=20">: Momentum is related to the change of the wave function: <img src="http://chart.apis.google.com/chart?cht=tx&chl=p%5E%5Cmu%3D%5Cpm%20i%5Chbar%5Cpartial_%5Cmu&chf=bg%2Cs%2CFFFFFF80&chco=000000">. The angular momentum of an atomic electron is quantized in units of <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Chbar%20%3D%201&chf=bg%2Cs%2CFFFFFF80&chco=000000&chs=20">.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cfrac1%7B%5Cvarepsilon_0%7D%3D%5Cmu_0%3D1&chf=bg%2Cs%2CFFFFFF80&chco=000000">: Electric and magnetic fields equations are clean and fundamental, especially <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cnabla%20%5Ccdot%20E%20%3D%20%5Crho&chf=bg%2Cs%2CFFFFFF80&chco=000000">. This defines [partially] rationalized Planck units. Charge becomes a dimensionless quantity, however the elementary charge is only close to 1, not 1.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cfrac1%7B%5Cvarepsilon_0%7D%3D%5Cmu_0%3D2%5Ctau&chf=bg%2Cs%2CFFFFFF80&chco=000000">: Often a <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cfrac1%7B2%5Ctau%7D&chf=bg%2Cs%2CFFFFFF80&chco=000000"> factor from diffusion in three dimensions (area of the 2-sphere) appears together with these constants (energy and force of point charges), therefore this system can be convenient. However this is not fundamental and creates counterintuitive constants in the fundamental equations. This is used in Gaußian cgs-units and standard Planck units. 
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=G%20%3D%201&chf=bg%2Cs%2CFFFFFF80&chco=000000">: This
takes a similar approach to the Gaußian units.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=G%20%3D%20%5Cfrac1%7B2%5Ctau%7D&chf=bg%2Cs%2CFFFFFF80&chco=000000">: This rationalizes the gravitational field as above and simplifies equations that are in some way related to areas of spheres. Creates Rationalized Planck units, the most fundamental natural units of these.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=G%20%3D%20%5Cfrac1%7B4%5Ctau%7D&chf=bg%2Cs%2CFFFFFF80&chco=000000">: This makes the equations of general relativity a bit cleaner.
* <img src="http://chart.apis.google.com/chart?cht=tx&chl=k_%7B%5Cmathrm%7BB%7D%7D%20%3D%201&chf=bg%2Cs%2CFFFFFF80&chco=000000">: Temperature is very much related to energy.

## Names of big and small values
Since the values of 1 in the different dimensions (as listed in the document) are not convenient yet, we need a system like kilo, Mega, Giga, ..., milli, micro, nano, ..., but systematic. I found it compelling to highlight those values that are (multiple of 10)-powers of 10, i.e. powers of <img src="http://chart.apis.google.com/chart?cht=tx&chl=10%5E%7B10%7D&chf=bg%2Cs%2CFFFFFF80&chco=000000">, which only for a relatively small base like six is usable. 
Since - like jan Misali - I like conlangs, especially lojban, the logical language, I thought of naming the exponents (divided by 10) like in lojban: 
* 0 = no, 1 = pa, 2 = re, 3 = ci [ʃi], 4 = vo [vo], 5 = mu, ... (there are named digits up to 23 (hexadecimal))
* Names of numbers are the concatenation of the digits: 10 = pano (alt. xa [xa]), 11 = papa (alt. ze [ze]), 12 = pare (alt. bi), ...
* The number unary minus (as in 'negative 3') is ni'u [nihu], which can - without interference with other words - be shortened to niu (I am not very happy using this one). For example -1254 = ni'u pa ki'o remuvo
* The digit point (not really encouraged to use in this system) is pi. For example <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Ctau%20%3D%2010.141100...%20%3D&chf=bg%2Cs%2CFFFFFF80&chco=000000"> pano pi pavopa panono...
Feel free to suggest different naming schemes at Issues.

So every power of <img src="http://chart.apis.google.com/chart?cht=tx&chl=10%5E%7B10%7D&chf=bg%2Cs%2CFFFFFF80&chco=000000"> will be assigned the name of the exponent expressed in lojban.
You can therefore call 3 eV a ni'u-pano-Energy or a second a paci-Time. (The dimension is optional, those values were in rationalized Planck units (6-RPU)). 
For more comparison values and SI values refer to the pdf-document in this repository. It was the original goal of this project and produced by python code that generated LaTeX code.
