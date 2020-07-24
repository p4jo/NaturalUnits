#region Setup

import numpy as n
document = ""

#endregion

#region Parameter
eps0_is_1 = True #1/4π otherwise
G_is_1 = False 
G8π_is_1 = False #1/4π otherwise
digits = 6
bases = [6,10,12]

prefixes = [["m",1E-3], ["",1], ["k",1E3]] #[["",1]] 

#endregion

#region Dimensionen [M,L,T,Q,Θ] und Basiseinheiten
M = n.array([1,0,0,0,0])
L = n.array([0,1,0,0,0])
T = n.array([0,0,1,0,0])
Q = n.array([0,0,0,1,0])
Θ = n.array([0,0,0,0,1])
E = n.array([1,2,-2,0,0])

f0 = 1.0
f1 = 1.0
if (eps0_is_1) :
    f0 = (4*n.pi)**(-1/2) 
if(G8π_is_1):
    f1 = (8*n.pi)**(-1/2)
elif (not G_is_1):
    f1 = (4*n.pi)**(-1/2)

p = [2.176434E-8*f1,1.616255E-35/f1,5.391247E-44/f1,1.876E-18*f0,1.416784E32*f1]

#endregion

#region Calculations

def inBaseStandard(base: int,value):
    global digits
    if (value == 0):
        return '0'
    pot = digits-1
    while n.abs(value) < base ** (digits-1):
        value *= base
        pot -= 1
    while n.abs(value) >= base ** digits:
        value /= base
        pot += 1
    s = n.base_repr(int(round((value))),base) + "\\cdot10^{" + str(n.base_repr(pot,base))+'}'
    return s[0] + '.' + s[1:]
    
def inBaseSpecial(base: int,value):
    global digits
    if digits <= base/2:
        digits = round(base/2)+1
    if (value == 0):
        return '0'
    pot = digits-1
    while n.abs(value) < base ** (digits-1):
        value *= base
        pot -= 1
    while n.abs(value) >= base ** digits:
        value /= base
        pot += 1
    potSpecial = round(pot/base)*base
    s = n.base_repr(int(round((value))),base) + "\\cdot10^{" + str(n.base_repr(potSpecial,base))+'}'
    i = potSpecial-pot
    if i > 0:
        res ="0."
        for _ in range (i-1):
            res += '0'
        return res + s
    else:
        return s[0:-i+1] + '.' + s[-i+1:]

inBase = inBaseSpecial

def inPlanckUnits(valSI,dim):
    for i in range(len(dim)):
        valSI /= p[i]**dim[i]
    return valSI
#endregion

#region Comparison values
comp = [
 ["Proton mass",1.67262192369E-27,M],
 ["Electron mass",9.10938356E-31,M],
 ["Elementary charge",1.60217662E-19,Q],
 ["1 Å",1E-10,L,"Length in atomic and solid state physics"],
 ["Bohr radius",5.29177210603E-11,L],
 ["Fine structure constant",7.2973525693E-3,[0,0,0,0,0]],
 ["Rydberg Energy",13.605693122994*1.60217662E-19,E],
 ["1 eV",1.60217662E-19,E],
 ["Earth g", 9.80665 ,M+L-T*2],
 ["1 cm",0.01,L],
 ["Liter",0.001,L*3],
 ["Area of a soccer field",7140,L*2],
 ["Hundred m²",100,L*2,"Size of a home"],

 ["Age of the Universe",662695992000000.0,T],
 ["Size of the observable Universe",8.8E26,L],
 ["Average density of the Universe",9.9E-33,M-L*3],
 ["Earth mass",5.972E24,M],
 ["Sun mass",1.98892E30,M],
 ["1 year",24*60*60*365.2425,T],
 ["1 parsec",3.0857E16,L],
 ["1 AE",149597870700.0,L],

 ["Stefan-Boltzmann constant",567052E-8,E-T-L*2-Θ*4],
 ["1 mol",6.02214086E23,[0,0,0,0,0]],
 ["Standard temperature 0°C",273.15,Θ],
 ["1 atm", 101325, M-L-T*2]
]

#endregion

#region output


def addLine(name,valueSI,dimension,base,color = '', comment = ''):
    global document
    
    β2 = n.base_repr(base-1)
    β2 += β2
    

    if color == '':
        color = 'black'
    
    if comment != '':
        comment = "\\footnote{" + comment + "}"

    valstr = inBase(base,inPlanckUnits(valueSI,dimension))

    document += "{\\color{" + color+ "}$" + name + comment + ' = ' + valstr +" $}"
    
    def stuff(out):
        global document
        for i in range(len(out)):
            if out[i] != '0' and out[i] != '.':
                out = out[i:]
                break
        if ("00" in out or β2 in out):
            document += "\\quad("
            while "00" in out:
                out = out.replace("00",'')
                document += "*"
            while β2 in out:
                out = out.replace(β2,'')
                document += "*"
            document += ")"
        else:
            pass

    stuff(valstr)

    document += "&\n\t"
    valstr = inBase(base,1/inPlanckUnits(valueSI,dimension))
    [mantissa,exp] = str.split(valstr,'\\cdot')
    exp = exp.replace('{','ß').replace('ß-','{').replace('ß','{-')
    pot = exp.replace('10^{','').replace('}','') + '-'
    document += "{\\color{" + color+ "}$ "+ nameOfExponent(pot,base) + "–" + writeDimension(dimension) + "=" + exp + " = " + mantissa +" \\cdot " + name +'$}'
    
    stuff(valstr)

    document += '\\\\\n'

def nameOfExponent(pot, base):
    return pot/base

def writeDimension(exponents,names = ["M","L","T","Q","Θ"]):
    num = ''
    den = ''
    for i in range(len(exponents)):
        if exponents[i] == 0:
            continue
        exp = abs(exponents[i])
        s = "\\operatorname{" + names[i] + "}" 
        if exp > 1:
            s += f"^{exp}"
        if exponents[i] < 0:
            den += s
        else:
            num += s
    if den == '':
        return num
    if num == '':
        return '\\frac1{' + den + '}'
    return '\\frac{' + num + '}{' + den + "}"

for base in bases:
    document += "\n\\chapter{Base " + str(base) + "}\n"

    document += "\\begin{center}\\begin{longtable}{l l}\n\\caption*{SI units: }\\\\\n"
    #region SI units
    for θ in [0,-1,1]:

        for q in [0,-1,1]:
            
                
            for m in [0,1]:
                document += "\\hline"
                document += ''
                for l in [0,1,2,-1,-2,-3]:
                    for t in [0,-1,-2,1]:
                        #if m + lp + tp + 3*n.min([qp,θp]) <= 7: #Only reasonable units
                        for prefix in prefixes: 
                            addLine("1 \\bm{\\mathrm{ " + prefix[0] +"}}"+ writeDimension([m,l,t,q,θ],['kg','m','s','C','K']),prefix[1],[m,l,t,q,θ],base,("gray" if prefix[0] != '' else ""))
                
    #endregion
    document += '\n\\caption*{Other interesting variables for comparison:}\\\\\n'
    
    for c in comp:
        addLine("\\textrm{"+c[0]+"}",c[1],c[2],base,comment=(c[3] if len(c) > 3 else ""))


    document += "\\end{longtable}\\end{center}"

print(document,file=open("NaturalUnits.tex",'w',encoding='utf-8'))

#endregion