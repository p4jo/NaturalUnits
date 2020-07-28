
#region Setup

import numpy as n
import numpy.linalg as nl
import re

M = n.array([1,0,0,0,0])
L = n.array([0,1,0,0,0])
T = n.array([0,0,1,0,0])
Q = n.array([0,0,0,1,0])
Θ = n.array([0,0,0,0,1])
E = n.array([1,2,-2,0,0])
p=[]
document = ''

#endregion

#region Parameter

def OnlyExponentsThatEndWithZero(pot): 
    return int(round(pot/base)*base)
def AllExponents(pot):
    return pot

def DividedByBase(pot:int):
    if pot == 0:
        return ''
    potStr = n.base_repr(pot,base)
    if potStr.endswith('0'):
        potStr = potStr[:-1]
    else: 
        potStr = potStr[:-1] + '.' + potStr[-1]
    return potStr

def DividedByBaseAndItalic(pot):
    text = DividedByBase(pot)
    if text == '':
        return ''
    return "\\textit{" + text + '}-'

def DividedByBaseInLojbanNumbering(pot:int):
    
    text = DividedByBase(pot)
    if text == '':
        return ''
    return text.replace('A','Dau').replace('B','Fei').replace('C','Gai').replace('D','Jau').replace('E','Rei').replace('F','Vai').replace('0','No').replace('1','Pa').replace('2','Re').replace('3','Ci').replace('4','Vo').replace('5','Mu').replace('6','Xa').replace('7','Ze').replace('8','Bi').replace('9','So').replace('-',"Ni'u").lower()+'-' 

#[True -> ε0 = 1; False -> 2τε0 = 1,
# True -> G=1 ,
# True -> G4τ = 1; False -> G2τ = 1]
Systems = [[True,True,False],[False,True,False],[True,False,False],[False,False,True]]

digits = 6
bases = [6,10,12]
prefixes =  [["m",1E-3], ["",1], ["k",1E3]] #[["",1]]#
namesOfExponents = [[OnlyExponentsThatEndWithZero,DividedByBaseAndItalic], [AllExponents,DividedByBaseAndItalic], [OnlyExponentsThatEndWithZero,DividedByBaseInLojbanNumbering]] #: (exponent)->LaTeX text string



base = 6
[eps0_is_1,G_is_1,G4τ_is_1] = [True,True,False]
PotRoundingFunction = OnlyExponentsThatEndWithZero
nameOfExponent = DividedByBaseInLojbanNumbering

def PrintSettings():
    print ("Base ",base,", ",nameOfExponent) #todo
#endregion


#region Calculations
def inBase(value:float):
    global digits, base
    if digits <= base/2:
        digits = round(base/2)+1
    if (value == 0):
        return ['0',0,0,'0','']
    
    sign = '-' if value < 0 else ''

    value = n.abs(value)

    baseToTheDigitsMinus1 = base ** (digits-1)
    approxPot = int(n.log2(value) / n.log2(base))
    pot = digits-1 + approxPot+1
    value *= base**(-approxPot-1)
    while n.round(value) < baseToTheDigitsMinus1:
        value *= base
        pot -= 1
    Pot = PotRoundingFunction(pot)
    mantissa = n.base_repr(int(round(value)),base)
    exp = "\\cdot10^{" + str(n.base_repr(Pot,base)) +'}' if pot != 0 else ''
    i = Pot-pot
    if i > 0:
        res ="0."
        for _ in range (i-1):
            res += '0'
        mantissa = res + mantissa
    else:
        mantissa = mantissa[0:-i+1] + '.' + mantissa[-i+1:]
    mantissa = sign + mantissa
    return [mantissa + exp, (value if sign == '' else -value), Pot, mantissa, exp]

Conv = nl.inv(n.array([[1,2,-1,0,0], [1,1,0,-2,0], [0,1,-1,0,0], [1,2,-2,0,-1], [-1,3,-2,0,0]]))

def SetupSystem():
    global p, eps0_is_1, G_is_1, G4τ_is_1
    f0 = 4*n.pi
    f1 = f0
    if (eps0_is_1) :
        f0 = 1.0
    if(G4τ_is_1):
        f1 *= 2.0
    elif (G_is_1):
        f1 = 1.0

    p = [6.62607015E-34/2/n.pi, 1.25663706212E-6 / f0, 299792458.0, 1.380649E-23, 6.67430E-11 *f1] 

def inPlanckUnits(valSI,dim):
    global p, Conv
    dim = n.matmul(n.array(dim), Conv) #Dimension Conversion
    for i in range(5):
        valSI /= p[i]**dim[i]
    return valSI
#endregion

#region output


def starRating(number, preDistance = '\\quad'):
    global base
    β2 = n.base_repr(base-1,base)
    β2 += β2
    result = ''
    for i in range(len(number)):
        if number[i] != '0' and number[i] != '.':
            number = number[i:]
            break
    if ("00" in number or β2 in number):
        result += preDistance + "("
        while "00" in number:
            number = number.replace("00",'0')
            result += "*"
        while β2 in number:
            number = number.replace(β2,β2[0])
            result += "*"
        result += ")"
    return result

def addLine(name,valueSI,dimension,color = '', comment = '', name2=''):
    global document

    if color != '':
        document += "\\color{" + color+ "}"

    if comment != '':
        comment = "\\footnote{" + comment + "}"

    if name2 == '':
        name2 =  "\\cdot " + name
    if name2 == '|':
        name2 = name
    if not name2.startswith('\\cdot'):
        name2 = '\\,' + name2
    
    [valstr,_,_,mantissa,_] = inBase(inPlanckUnits(valueSI,dimension))

    document += "$"+name + comment + ' = ' + valstr +" $"
    document += starRating(mantissa) + "&\n\t"
    if color != '':
        document += "\\color{" + color+ "}"
    [valstr,_,pot,mantissa,exp] = inBase(1/inPlanckUnits(valueSI,dimension))

    if pot != 0:
        exp = exp.replace('\\cdot','').replace('{','ß').replace('ß-','{').replace('ß','{-')
    else:
        exp = '1'
    document += "$1\\:\\text{"+ nameOfExponent(-pot) + "} " + writeDimension(dimension) + "=" + exp + " = " + mantissa + name2 +'$'
    
    document += starRating(mantissa) + '\\\\\n'



def writeDimension(exponents,names = ["M","L","T","Q","\\Theta"],operatorname = False):
    num = ''
    den = ''
    for i in range(len(exponents)):
        if exponents[i] == 0:
            continue
        exp = abs(exponents[i])
        if operatorname:
            s = "\\operatorname{" + names[i] + "}" 
        else:
            s = names[i]
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

def baseReplace(text):
    parts = text.split('ß')
    for i in range(len(parts)):
        try:
            parts[i] = n.base_repr(int(parts[i]),base)
        except:
            pass
    return ''.join(parts)
        

#endregion
#region Document
def CreateDocument():
    global document,base,eps0_is_1,G_is_1,G4τ_is_1

    #region Comparison values
    comp = [
    ["Proton mass",1.67262192369E-27,M,True,'','m_p'],
    ["Electron mass",9.10938356E-31,M,True,'','m_e'],
    ["Elementary charge",1.60217662E-19,Q,True,'','e'],
    ["\\si\\angstrom",1E-10,L,False,"Length in atomic and solid state physics, 1/ß10ß nm",'|'],
    ["Bohr radius",5.29177210603E-11,L,True,'Characteristic Length in the hydrogen atom','r_B'],
    ["Fine structure constant",7.2973525693E-3,[0,0,0,0,0],True,'','\\alpha'],
    ["Rydberg Energy",13.605693122994*1.60217662E-19,E,True,'','Ry'],
    ["\\si\\eV",1.60217662E-19,E,False,'','|'],
    ["\\hbar",6.62607015E-34/2/n.pi,E+T,False,"Quantum of angular momentum, Ratio between frequency (space/time) and momentum (momentum/Energy)"],
    ["\\lambda_\\mathrm{yellow}",575E-9,L],
    ["k_\\mathrm{yellow}",2*n.pi/575E-9,-L,False,"τ/λ = k = ω = p = E (In natural units - i.e. in these units)"],
    ["k_\\mathrm{X-Ray}",5.96075295947766E17,-L,False,'Geometric mean of upper and lower end of X-Ray definitions'],
    [],
    ["Earth g", 9.80665 ,M+L-T*2,True],
    ["\\si\\cm",0.01,L,False,'','|'],
    ["\\si\\min",60,T,False,'','|'],
    ["hour",60*60,T,True,'','\\operatorname h'],
    ["Liter",0.001,L*3,True,'','l'],
    ["Area of a soccer field",7140,L*2,True,'','A'],
    ["ß100ß \\operatorname m^2",100,L*2,False,"Size of a home"],
    ["km/h",1/3.6,L-T,True,'','|'],
    ["mi/h",0.44704,L-T,True,'','|'],
    ["inch",0.0254,L,True,"ß36ß in = 1 yd = 3 ft",'|'],
    ['mile',1609.3,L,True,'','|'],
    ['pound',0.45359237,M,True,'','|'],
    ["horsepower",745.7,E-T,True,'','|'],
    ["kcal",4186.8,E,True,'','|'],

    [],
    ["Age of the Universe",662695992000000.0,T,True,'','t_U'],
    ["Size of the observable Universe",8.8E26,L,True,'','l_U'],
    ["Average density of the Universe",9.9E-33,M-L*3,True,'','\\rho_U'],
    ["Earth mass",5.972E24,M,True,'','m_E'],
    ["Sun mass",1.98892E30,M,True,'','m_S'],
    ["Year",24*60*60*365.2425,T,True,'','\\operatorname y'],
    ["c",299792458,L-T],
    ["Parsec",3.0857E16,L,True,'','\\operatorname{pc}'],
    ["Astronomical unit",149597870700.0,L,True,'','\\operatorname{AE}'],
    [],
    ["Stefan-Boltzmann constant",567052E-8,E-T-L*2-Θ*4,True,'','\\sigma'],
    ["\\si{\\mol}",6.02214086E23,[0,0,0,0,0],False,'','|'],
    ["Standard temperature",273.15,Θ,True,"0°C measured from absolute zero","T_0"],
    ["Room - standard temperature",20,Θ,True,"ß20ß °C",'\\Theta_R'],
    ["atm", 101325, M-L-T*2,True,'','|'],
    ["c_s",343,L-T],
    [],
    ["\\mu_0",1.25663706212E-6,M+L-Q*2],
    ["G",6.67430E-11,L*3-M-T*2],
    ]

    #endregion

    for SYSTEM in Systems:
        [eps0_is_1,G_is_1,G4τ_is_1] = SYSTEM
        #region Dimensionen [M,L,T,Q,Θ] und Basiseinheiten
        text = ''
        if len(Systems) == 1:
            scope = "document"
            partName = ''
        else:
            scope = "part"
            partName = "\\nameref{part"+str(eps0_is_1)+str(G_is_1)+str(G4τ_is_1)+"}"
            text += "\\part{Unnamed Natural Units}\\label{part"+str(eps0_is_1)+str(G_is_1)+str(G4τ_is_1)+"}\n"
        text += "{\\large This " + scope +" uses natural units, where $\\epsilon_0 = "
        
        if eps0_is_1:
            text += "1"
        else:
            text += "\\frac1{2\\tau}"
        text += "$ and $G="
        if G4τ_is_1:
            text += "\\frac1{4\\tau}"
        elif G_is_1:
            text += "1"
        else:
            text += "\\frac1{2\\tau}"
        text += "$. "

        if G_is_1 and not eps0_is_1:
            text += "These are the usual Planck units."
            text = text.replace("Unnamed Natural Units","Usual Planck units")
        if G_is_1 and eps0_is_1:
            text += "These are partially rationalized Planck units."
            text = text.replace("Unnamed Natural Units","Partially Rationalized Planck units")
        if not G4τ_is_1 and not G_is_1 and eps0_is_1:
            text += "These are rationalized Planck units."
            text = text.replace("Unnamed Natural Units","Rationalized Planck units")
        text += "}"

        document += text

        SetupSystem()

        # [hbar,µ_0,c,k_B,G] in dimensions [ML²/T,ML/Q²,L/T,ML²/T²/Θ²,1/M L³/T²]]. µ0 ist genau bekannt, G ungenau, die anderen exakt
        #endregion
        for BASE in bases:
            base = BASE
            document += "\n\\chapter{Base " + str(base) + " - " + partName + "}\n"
            print(base)
            for [PRF,noE] in namesOfExponents:   
                PotRoundingFunction = PRF
                nameOfExponent = noE
                document += "\n\\section{" + ' '.join(re.findall('[A-Z][^A-Z]*',PotRoundingFunction.__name__))+ " will be used and displayed as " + ' '.join(re.findall('[A-Z][^A-Z]*',nameOfExponent.__name__)) +"}"
                document += "\\begin{longtable}{l l}\n"
                #region Comparison values
                document += '\n\\caption*{Interesting variables for comparison:}\\\\\n'
                
                for c in comp:
                    if len(c) > 2:
                        name = c[0]
                        if len(c) > 3 and c[3]:
                            name = "\\textrm{"+name+"}"
                        addLine(baseReplace(name), c[1], c[2], comment=(baseReplace(c[4]) if len(c) > 4 else ""),name2=(baseReplace(c[5]) if len(c) > 5 else ''))
                    else:
                        document += "\\\\\n"

                #endregion
                #region SI units
                document += "\\caption*{Extensive list of SI units}\\\\\n"
                for θ in [0,-1,1]:
                    document += "\\arrayrulecolor{black}\\hline\n"
                    for q in [0,-1,1]:
                        if q != 0 and θ < 0:
                            continue
                        document += "\\arrayrulecolor{gray}\\hline\n"

                        for m in [0,1]:
                            document += "\\arrayrulecolor{light-gray}\\hline\n"
                            document += ''
                            for l in [0,1,2,-1,-2,-3]:
                                for t in [0,-1,-2,1]:
                                    #if m + lp + tp + 3*n.min([qp,θp]) <= 7: #Only reasonable units
                                    for prefix in prefixes: 
                                        name = "\\bm{\\mathrm{ " + prefix[0] +"}}"+ writeDimension([m,l,t,q,θ],['kg','m','s','C','K'],True)
                                        addLine("1 "+name,prefix[1],[m,l,t,q,θ],("gray" if prefix[0] != '' else ""),name2=name)
                            
                #endregion
                

                document += "\\end{longtable}"

    print(document,file=open("NaturalUnits.tex",'w',encoding='utf-8'))

#endregion

#region main
def SetExpRule():
    global PotRoundingFunction
    PotRoundingFunction=eval(input("Set Rule (AllExponents or OnlyExponentsThatEndWithZero): "))

def inExpr(i,string):
    # expressions = string.split(' ')
    # for expr in expressions:
    #     if i < len(expr):
    #         string = expr
    #         break
    #     i -= len(expr)

    # if ':' in string:
    #     if string.find(':') < i:
    #         return True
    # if ';' in string:
    #     if string.find(';') < i:
    #         return True
    j = i
    while j >= 0:
        j -= 1
        if string[j] == ';' or string[j] == ':':
            return True
        if string[j] == ' ':
            return False
    return False


def Evaluate(inputString:str):
    inputString = inputString.strip()
    if inputString == '#':
        return Ans
    
    for i in range(len(inputString)):
        c = inputString[i]
        if inExpr(i,inputString) or (c == '-' and i>0 and inputString[i-1] == 'E'):
            pass
        else:
            if c == '-':
                inputString = inputString[:i] + '_' + inputString[i+1:]
            if c == '+':
                inputString = inputString[:i] + '†' + inputString[i+1:]
            if c == '/' or c == '\\':
                inputString = inputString[:i] + '\\' + inputString[i+1:]
            if c == '*':
                inputString = inputString[:i] + '·' + inputString[i+1:]

    inputString = inputString.replace('_','†~').replace('\\','·÷').replace('††','†').replace('··','·')

    summands = inputString.split('†')
    #print(summands)
    if len(summands) > 1:
        result = 0
        for summand in summands:
            if summand.startswith('~'):
                result -= Evaluate(summand[1:])
            else:
                result += Evaluate(summand)
        return result

    factors = inputString.split('·')
    if len(factors) > 1:
        result = 1
        for factor in factors:
            if factor.startswith('÷'):
                result /= Evaluate(factor[1:])
            else:
                result *= Evaluate(factor)
        return result
            
    if ';' in inputString:
        f = 1
    if ':' in inputString:
        f = -1
        inputString = inputString.replace(':',";")
    inputValue = 0.0
    Dim=[0,0,0,0,0]
    for comm in inputString.split(';'):
        if comm == '':
            continue
        if inputValue == 0:
            try:
                stuff = (comm+'E0').split('E')
                mantissa = stuff[0]
                if not '.' in mantissa:
                    mantissa += '.'
                exp = stuff[1]
                inputValue = int(mantissa.replace('.',''),inputBase) * inputBase**(int(exp,inputBase) - (len(mantissa) - 1 - mantissa.index('.') ))
            except Exception as e:
                print(e)
                continue

        elif inputValue != 0:
            try:
                Dim = f*eval(comm)
            except Exception as e:
                print(e)
                continue
    return inPlanckUnits(inputValue,Dim)
    
commands = {"exit": lambda:exit(),  
            "SetExpRule": SetExpRule}
PrintSettings()
SetupSystem()
inputBase = base
Ans = 0
while True:
    inputString = input()
    if inputString == '':
        continue
    if inputString in commands:
        commands[inputString]()
        continue
    if re.match("[0-9=\\-+]",inputString[0]):
        if inputString[0] == '=':
            inputString = inputString[1:]
        Ans = Evaluate(inputString)
        [_,_,pot,valStr,_] = inBase(Ans)
        #[m,l,t,q,θ] = Dim
        print(valStr +' '+nameOfExponent(pot))#+f"M^{m}·L^{l}·T^{t}·Q^{q}·Θ^{θ}")

    else:
        try:
            print(eval(inputString))
        except Exception as e:
            try:
                exec(inputString)
            except Exception as e:
                print(e)
                continue


#endregion
