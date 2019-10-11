from .number_theory import (
    gcdext,
    is_coprime,
    reverse,
    prod
)


class ModSpace(object):
    def __init__(self, n: int, m: int):
        self.n: int = n
        self.m: int = m

    def gcdext(self, g: int = 0, t: int = 0, u: int = 0) -> tuple:
        return gcdext(self.n, self.m, g, t, u)

    def is_coprime(self):
        return is_coprime(self.n, self.m)

    @property
    def reverse(self):
        return reverse(self.n, self.m)

    def __str__(self):
        return f"{self.n} (ModSpace {self.m})"
