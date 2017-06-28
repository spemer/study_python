from classFirstFunc import _calc

_c = _calc(0,0)
_c.v1 = int(input("Numb 1: "))
_c.v2 = int(input("numb 2: "))
print()


print("%d + %d = %d" % (_c.v1, _c.v2, _c.add() ))
print("%d - %d = %d" % (_c.v1, _c.v2, _c.sub() ))
print("%d * %d = %d" % (_c.v1, _c.v2, _c.mul() ))
print("%d / %d = %d" % (_c.v1, _c.v2, _c.div() ))
print()