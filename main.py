from sympy import *
from sympy.plotting import plot, plot3d

x, y, z = symbols('x y z')


# print math expressions with correct characters
def p(x):
    x = str(x)
    x = x.replace("**", "^")
    x = x.replace("*", "·")
    print(x)

'''
# integrate
i = integrate(sin(x), (x))
p(i)
i = integrate(sin(x), (x, 0, pi/2))
p(i)

i = integrate(z, (x), (y), (z))
p(i)

# plotting some func
d = integrate(x, (x), (y))
plot3d(d, (x, -10, 10), (y, -10, 10))
c = integrate(x, (x))
plot(c, (x, 10, 20))
'''

'''
///////////////////////////////////
'''
from sympy import Curve, line_integrate, E, ln

x, y, t = symbols("x y t")

C = Curve([E**t +1, E**t -1], (t, 0, ln(2)))
i = line_integrate(x+y, C, [x,y])
p(i)
