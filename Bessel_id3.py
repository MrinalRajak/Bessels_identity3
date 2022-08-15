
#Bessel's identity
#(3) jn(0,x) = (2/π)*∫_(t=0)^1▒(cos⁡(xt)/√(1-t^2 ))dt

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))

def f(t):
    return (2/np.pi)*(np.cos(x*t)/(np.sqrt(1-t**2)))

LHS=jn(0,x)
RHS=quad(f,0.0,1.0)[0]

print("LHS: ",LHS)
print("RHS: ",RHS)
