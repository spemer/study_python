from classFirstFunc import _calc

_c = _calc(0,0)
_c.v1 = int(input("Numb 1: "))
_c.v2 = int(input("numb 2: "))
print()

########## numb ##########

print("Numb 1: %d" % _c.getValue())
print("Numb 2: %d" % _c._getValue())
print()

_c.setValue(_c.v1)
_c.setValue(_c.v2)

########## calc ##########

print("%d + %d = %d" % (_c.v1, _c.v2, _c.add() ))
print("%d - %d = %d" % (_c.v1, _c.v2, _c.sub() ))
print("%d * %d = %d" % (_c.v1, _c.v2, _c.mul() ))
print("%d / %d = %d" % (_c.v1, _c.v2, _c.div() ))