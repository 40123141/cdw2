from sympy import *
# center ot radius 40
x1 = Symbol('x1')
y1 = Symbol('y1')
# upper tangent point
x2 = Symbol('x2')
y2 = Symbol('y2')
# lower tangent point
x3 = Symbol('x3')
y3 = Symbol('y3')
answer = solve([x2**2 + y2**2 - 7*7, (x1-x2)**2+(y1-y2)**2 -40**2, (x1-x3)**2+(y1-y3)**2 -40**2, (x1)**2+(y1)**2 -47**2, \
       (x1)**2+(y1+20)**2 -47**2, x2-x3], [x1, y1, x2, y2, x3, y3])
group = 1
for i in answer:
    print("group", group, ":")
    for j in i:
        print(j.evalf(5))
    group += 1
