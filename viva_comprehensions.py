import math
from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    Generate list of integers within specified range based on parity condition.

    :param start: The starting value of range which is inclusive.
    :param stop: Ending value of range is exclusive.
    :param parity: parity condition (ODD or EVEN) to filter generated list.
    :return: A list of integers within range based on parity.
    """

    return [num for num in range(start, stop) if num % 2 != parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    return {x: strategy(x) for x in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    return {x.upper() for x in val_in if x.lower() in val_in}

    # This works as well; maybe even better~
    # return {x.upper() for x in set(val_in) if x.islower()}
