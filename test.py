from ycrypto import (
    ModSpace,
    number_theory,
    formulas
)


def gcdext():
    assert (3, 1, 0) == number_theory.gcdext(3, 6)
    assert (1, -3, 1) == number_theory.gcdext(5, 16)


def chiene_remainder_theorem():
    assert 932, formulas.chiene_remainder_theorem(ModSpace(
        9, 13), ModSpace(8, 11), ModSpace(1, 7))
    assert 301, formulas.chiene_remainder_theorem(
        ModSpace(1, 3), ModSpace(1, 4), ModSpace(1, 5), ModSpace(0, 7))


def prime():
    prime_list = ["104677", "104681", "104683", "104693",
                  "104701", "104707", "104711", "104717", "104723", "104729", ]

    for prime in prime_list:
        assert True, number_theory.is_prime(prime)
        assert True, number_theory.is_prime_basic(prime)


if __name__ == "__main__":
    gcdext()
    chiene_remainder_theorem()
    prime()
