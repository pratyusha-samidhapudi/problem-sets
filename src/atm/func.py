"""
ATM package functions

"""

from typing import List, Optional, Tuple

COINS = 50, 25, 10, 5, 2, 1
BILLS = 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00
DENOMINATIONS = BILLS + COINS


def withdraw(amount: int,
             denominations: Optional[Tuple[int]] = DENOMINATIONS
             ) -> List[Tuple[int, int]]:
    if amount <= 0:
        return []

    size: int = len(denominations)
    multipliers = [0] * size

    for idx in range(size):
        multipliers[idx] = amount // denominations[idx]
        amount -= multipliers[idx] * denominations[idx]

    # filter zero multipliers
    filtered = filter(lambda pair: pair[0] > 0, zip(multipliers, denominations))

    return list(filtered)


def withdraw_rev(amount: int,
                 limit: Optional[int] = 10,
                 denominations: Optional[Tuple[int]] = DENOMINATIONS
                 ) -> List[Tuple[int, int]]:
    # TODO: add function implementation
    raise NotImplementedError


def get_total(amount: List[Tuple[int, int]]) -> int:
    balance = 0
    for multiplier, denomination in amount:
        balance += multiplier * denomination

    return balance


if __name__ == "__main__":
    print(F"{withdraw_rev(13)}")
