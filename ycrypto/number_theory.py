import math
import random


def prod(numbers: list) -> int:
    """Verilen listedeki tüm elemanları çarpar

    Arguments:
        numbers {list} -- Sayı listesi

    Returns:
        int -- Çarpımın sonucu
    """
    result = 1
    for number in numbers:
        result *= number
    return result


def is_coprime(n: int, m: int):
    """Aralarında asallık kontrolü

    Arguments:
        n {int} -- Sayı
        n {int} -- Sayı

    Returns:
        bool - Aralarında asalsa True
    """
    return math.gcd(n, m) == 1


def gcdext(n: int, m: int, g: int = 0, t: int = 0, u: int = 0) -> tuple:
    """Modüler uzayda sayının tersini alma

    Arguments:
        n {int} -- Sayı1
        m {int} -- Sayı2

    Keyword Arguments:
        g {int} -- t.n + u.m (1 ise tersi vardır)
        t {int} -- Sayı1'in Sayı2 modüler uzayında tersi (default: {0})
        u {int} -- Sayı2'in Sayı1 modüler uzayında tersi (default: {0})

    Returns:
        tuple -- gcd(n,m), n^-1 (mod m), m^-1 (mod n)
    """
    if m == 0:
        g, t, u = n, 1, 0
    else:
        g, t, u = gcdext(m, n % m, g, t, u)
        s = u
        u = t - math.floor(n / m) * u
        t = s
    return g, t, u


def reverse(n: int, m: int) -> int:
    """n^-1 (mod m) işlemini gerçekler

    Arguments:
        n {int} -- Sayı
        m {int} -- Modüler uzay

    Return:
        int -- n^-1 (mod m)
    """
    result = gcdext(n, m)
    if result[0] != 1:
        return 0
    else:
        return result[1] % m


def is_prime(p: int) -> bool:
    """Asal sayı kontrolü

    Arguments:
        p {int} -- Asallığı kontrol edilecek sayı

    Returns:
        bool - Asalsa True
    """
    for n in range(int(math.sqrt(p))):
        if p % n == 0:
            return False
    return True


def is_prime_basic(p: int) -> bool:
    """Sözde asallar ile asal sayı kontrolü

    Arguments:
        p {int} -- Asallığı kontrol edilecek sayı

    Returns:
        bool - Asalsa True
    """
    return (2 ** (p - 1) % p) == 1


def ferman_theroem(n: int, m: int) -> bool:
    """Ferman teoremi ile asal sayı kontrolü

    Arguments:
        p {int} -- Asallığı kontrol edilecek sayı

    Returns:
        bool - Asalsa True
    """
    if is_coprime(n, m):
        return ((n ** (m - 1)) % m) == 1
    return False
