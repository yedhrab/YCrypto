from .mod_space import ModSpace
from .number_theory import(
    prod,
    reverse
)


def chiene_remainder_theorem(*modspaces: ModSpace) -> int:
    """Çinli Kalanlar Teoremi ile modüler uzayda sonuç bulur

    Returns:
        int -- Sonuç
    """
    space_number = len(modspaces)
    m, n = [], []

    for modspace in modspaces:
        m.append(modspace.m)
        n.append(modspace.n)

    m_prod = prod(m)

    M, y = [], []
    for i in range(space_number):
        M.append(int(m_prod / m[i]))
        y.append(reverse(M[i], m[i]))

    result = 0
    for i in range(space_number):
        result += n[i] * M[i] * y[i]

    return result % m_prod
