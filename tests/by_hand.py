from proofer.base import Symbol, Operation


@Operation
def add(a, b):
    return a() + b()


# (a + b)^2
# (a + b)*(a + b)
# a*(a + b) + b*(a + b)
# a*a + a*b + b*a + b*b
# a*a + a*b + a*b + b*b
# a*a + 2*a*b + b*b
# a^2 + 2*a*b + b*b
# a^2 + 2*a*b + b^2
