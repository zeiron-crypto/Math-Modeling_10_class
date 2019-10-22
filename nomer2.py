from nomer import g
from numpy import cos, tan, sqrt, pi
h=100
b=30
a=pi/3
v=sqrt(g*h*(1/tan(b)**2*b/2*(cos(a)**2*(1-(1/tan(b))*(1/tan(a))))))
print(v)
T=200
c=300
from nomer import k
from numpy import e
N=2/sqrt(pi)*h/(k*T)**(3/2)*e**(-c/k*T)*c**(T/2)
print(N)
