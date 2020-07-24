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
def inBase(base: int,value):
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

def inPlanckUnits(valSI,dim):
    for i in range(len(dim)):
        valSI /= p[i]**dim[i]
    return valSI
#endregion

#region Comparison values
comp = [
 ["Proton mass",1.67262192369E-27,M],
 ["Electron mass",9.10938356E-31,M],
 ["Earth g",9.81,M+L-T*2],
 ["Age of the Universe",662695992000000.0,T],
 ["Size of the observable Universe",8.8E26,L],
 ["Average density of the Universe",9.9E-33,M-L*3],
 ["Elementary charge",1.60217662E-19,Q],
 ["1 mol",6.02214086E23,[0,0,0,0,0]],
 ["1 year",24*60*60*365.2425,T],
 ["1 parsec",3.0857E16,L],
 ["1 AE",149597870700.0,L],
 ["1 Å",1E-10,L],
 ["Bohr radius",5.29177210603E-11,L],
 ["Fine structure constant",7.2973525693E-3,[0,0,0,0,0]],
 ["Earth mass",5.972E24,M],
 ["Sun mass",1.98892E30,M],
 ["1 eV",1.60217662E-19,E],
]

#endregion

#region output


def addLine(name,valueSI,dimension,color = ''):
    global document
    if color == '':
        color = 'black'
    out = "{\\color{" + color+ "}$" + name + ' = ' + inBase(base,inPlanckUnits(valueSI,dimension))+" $}"
    if ("00" in out):
        out += "\\quad(*)"
    else:
        out += '  '

    document += out + " & "
    
    out = "{\\color{" + color+ "}$ 1 = " + inBase(base,1/inPlanckUnits(valueSI,dimension)) +" \\cdot " + name +'$}'
    if ("00" in out):
        out += "\\quad(*)"
    else:
        out += '  '

    document += out + '\\\\\n'

for base in bases:
    document += "\n\\chapter{Base " + str(base) + ":}\n"

    document += "\\begin{center}\\begin{longtable}{l l}\\caption*{SI units: }\\\\"
    #region SI units
    for θ in range (-1,2):
        sθ = ""
        θp = θ
        if θ < 0:
            θp = -θ
            sθ = '\\frac1{'              
        else:
            sθ = '{'
        if θp == 0:
            sθ += ""
        if θp >= 1:
            sθ += "\\operatorname{K}" 
        if θp > 1:
            sθ += f"^{θp}"
        sθ += '}'
        
        for q in range (0,2):
            sq = ""
            qp = q
            if q < 0:
                qp = -q
                sq = '\\frac1{'
            else:
                sq = '{'
            if qp == 0:
                sq += ""
            if qp >= 1:
                sq += "\\operatorname{C}" 
            if qp > 1:
                sq += f"^{qp}"
            sq+='}'
            for m in range(2):
                document += "\\hline"
                document += ''
                if m == 0:
                    sm = ""
                elif m == 1:
                    sm = "\\operatorname{kg}"
                for l in range(-3,3):
                    sl = ""
                    lp = l
                    if l < 0:
                        lp = -l
                        sl = '\\frac1{'
                    else:
                        sl = '{'
                    if lp == 0:
                        sl += ""
                    if lp >= 1:
                        sl += "\\operatorname{m}" 
                    if lp > 1:
                        sl += f"^{lp}"
                    sl += '}'
                    for t in range(-2,2):
                        st = ""
                        tp = t
                        if t < 0:
                            tp = -t
                            st = '\\frac1{'
                        else:
                            st = '{'
                        if tp == 0:
                            st += ""
                        if tp >= 1:
                            st += "\\operatorname{s}" 
                        if tp > 1:
                            st += f"^{tp}"
                        st += '}'
                        if m + lp + tp + 3*n.min([qp,θp]) <= 7: #Only reasonable units
                            for prefix in prefixes: 
                                addLine("1 \\bm{\\mathrm{ " + prefix[0] +"}}"+ sm + sl + st + sq + sθ,prefix[1],[m,l,t,q,θ],("gray" if prefix[0] != '' else ""))
                
    #endregion
    document += '\\caption*{Other interesting variables:}\\\\'
    
    for c in comp:
        addLine("\\textrm{"+c[0]+"}",c[1],c[2])

    document += "\\end{longtable}\\end{center}"

print(document,file=open("NaturalUnits.tex",'w',encoding='utf-8'))

#endregion