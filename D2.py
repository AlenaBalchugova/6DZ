class Road:
    l = 20
    w = 1

    def __init__(self,
                 l,
                 w,
                 weight,
                 depth):
        self._length = l
        self.w = w
        self.weight = weight
        self.depth = depth
    def mass(self):
        leng = self.l
        wid = self.w
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Асфальт массой \n {leng} метр * {wid} метр * {w} кг * {dep} см = ", total, "т")
r = Road( 20, 5000, 25, 5)
r.mass()