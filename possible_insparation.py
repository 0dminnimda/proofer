from sympy.solvers import solve
import sympy as sp

# x = sp.symbols('x')
# a = sp.Integral(sp.cos(x)*sp.exp(x), x)
# sp.Eq(a, a.doit())

x, y, m = sp.symbols('x y m', integer=True, positive=True, nonzero=True)
m1, m2 = solve((x**2 + 4*y**2)**2 + 4*m*y*(x**2 + 4*y**2) - m**2*x**2, m)

d_m1 = sp.diff(m1, x, y)
d_m2 = sp.diff(m2, x, y)

d_m1 *= x
d_m2 *= x

d_m1 /= 4
d_m2 /= 4

# d_m1 *= -1

d_m1 = sp.cancel(d_m1)
d_m2 = sp.cancel(d_m2)

d_m1 *= x**2
d_m2 *= x**2

d_m1 *= sp.sqrt(x**2 + 4*y**2)
d_m2 *= sp.sqrt(x**2 + 4*y**2)

d_m1 = sp.simplify(d_m1)
d_m2 = sp.simplify(d_m2)

d_m1 /= 3 * y
d_m2 /= 3 * y

d_m1 /= 4 * y
d_m2 /= 4 * y

d_m1 = sp.simplify(d_m1)
d_m2 = sp.simplify(d_m2)

ot = sp.sqrt(x**2 + 4*y**2)

d_m1 += ot
d_m2 += ot

d_m1 **= 2
d_m2 **= 2
ot **= 2

d_m1 -= ot
d_m2 -= ot

d_m1 = sp.cancel(d_m1)
d_m2 = sp.cancel(d_m2)

d_m1 *= 16*y**2
d_m2 *= 16*y**2

# m1.subs({x:0})

sp.pprint(m1)
sp.pprint(m2)

sp.pprint(d_m1)
sp.pprint(d_m2)

breakpoint
