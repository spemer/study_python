class _calc(object):
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2

########## calc ##########

    def add(self):
        return self.v1 + self.v2

    def sub(self):
        return self.v1 - self.v2

    def mul(self):
        return self.v1 * self.v2

    def div(self):
        return self.v1 / self.v2

########## numb ##########

    def getValue(self):
        return self.v1

    def setValue(self, v1):
        self._v1 = v1

    def _getValue(self):
        return self.v2

    def _setValue(self, v2):
        self._v2 = v2