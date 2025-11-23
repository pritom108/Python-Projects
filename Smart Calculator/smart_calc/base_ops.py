from typing import Tuple


class BaseOps:
    @staticmethod
    def to_base(n: int, base: int) -> str:
        if base < 2 or base > 36:
            raise ValueError('base must be between 2 and 36')
        if n == 0:
            return '0'
        neg = n < 0
        n = abs(n)
        digits = []
        while n:
            d = n % base
            if d < 10:
                digits.append(str(d))
            else:
                digits.append(chr(ord('A') + d - 10))
            n //= base
        if neg:
            digits.append('-')
        return ''.join(reversed(digits))


    @staticmethod
    def from_base(s: str, base: int) -> int:
        s = s.strip()
        return int(s, base)


    @staticmethod
    def ones_complement(bitstring: str) -> str:
        return ''.join('1' if c == '0' else '0' for c in bitstring)


    @staticmethod
    def twos_complement(bitstring: str) -> str:
        # assume bitstring is binary
        n = int(bitstring, 2)
        mask = (1 << len(bitstring)) - 1
        twos = ((~n) + 1) & mask
        return format(twos, '0{}b'.format(len(bitstring)))


    @staticmethod
    def pad_bits(bitstring: str, bits: int) -> str:
        s = bitstring.replace('_', '')
        if len(s) > bits:
            raise ValueError('bitstring longer than bits')
        return s.zfill(bits)