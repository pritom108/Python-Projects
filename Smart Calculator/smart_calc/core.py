from typing import Tuple
import math
import cmath


class CalcError(Exception):
    pass




def parse_angle_deg(angle_str: str) -> float:
    """Parse angle string and return float degrees. Accepts plain numbers."""
    try:
        return float(angle_str)
    except Exception:
        raise CalcError(f"Invalid angle value: {angle_str}")




def clamp_int(n: int, bits: int) -> int:
    """Clamp integer value into signed range of given bits."""
    max_val = (1 << (bits - 1)) - 1
    min_val = - (1 << (bits - 1))
    if n > max_val or n < min_val:
        raise CalcError(f"Value {n} out of signed {bits}-bit range")
    return n