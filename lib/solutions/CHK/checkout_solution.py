from typing import Dict, Tuple


def chk_r1_info():
    prices_A = {
        1: 50,
        3: 130,
    }
    prices_B = {
        1: 30,
        2: 45,
    }
    price_A1 = {"multi": 3, "price": 130}
    price_A2 = {"multi": 1, "price": 50}
    price_B1 = {"multi": 2, "price": 45}
    price_B2 = {"multi": 1, "price": 30}
    price_C1 = {"multi": 1, "price": 20}
    price_D1 = {"multi": 1, "price": 15}
    info = {
        "A": [price_A1, price_A2],
        "B": [price_B1, price_B2],
        "C": [price_C1],
        "D": [price_D1],
    }
    return info


def chk_r2_info():
    price_A1 = {"multi": 5, "price": 200}
    price_A2 = {"multi": 3, "price": 130}
    price_A3 = {"multi": 1, "price": 50}
    price_B1 = {"multi": 2, "price": 45}
    price_B2 = {"multi": 1, "price": 30}
    price_C1 = {"multi": 1, "price": 20}
    price_D1 = {"multi": 1, "price": 15}
    price_E1 = {"multi": 2, "price": 40}
    price_E2 = {"multi": 1, "price": 40}
    info = {
        "A": [price_A1, price_A2],
        "B": [price_B1, price_B2],
        "C": [price_C1],
        "D": [price_D1],
        "E": [price_E1, price_E2],
    }
    return info


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    chk_r2 = Checkout(chk_r2_info())
    try:
        counts = chk_r2.parse_SKUs(skus)
    except ValueError:
        return -1
    return chk_r2.get_best_price_all(counts)


def checkout_r1(skus):
    chk_r1 = Checkout(chk_r1_info())
    try:
        counts = chk_r1.parse_SKUs(skus)
    except ValueError:
        return -1
    return chk_r1.get_best_price_all(counts)


class Checkout:
    def __init__(
            self,
            price_table: Dict[str, Dict]
            ):
        self.price_table = price_table

    def get_best_price(
            self,
            item_name: str,
            count: int
            ):
        running_total = 0
        all_prices = item_info["offer"] + [{"multi": 1, "price": item_info["price"]}]
        for offer in all_prices:
            how_many_offers = count // offer["multi"]
            running_total += how_many_offers * offer["price"]
            count %= offer["multi"]
        return running_total

    def get_best_price_all(
            self,
            counts: Dict[str, int],
            ) -> int:
        # counts is a Dict of "item_name": item_counts
        best_prices = [
            self.get_best_price(name, count)
            for name, count in counts.items()
        ]
        return sum(best_prices)

    def parse_SKUs(self, skus: str) -> Dict[str, int]:
        # if input only contains letters that we stock,
        # return a dictionary of counts. Else raise
        # a ValueError
        counts = {name: 0 for name in self.price_table.keys()}
        for c in skus:
            if c not in counts:
                raise ValueError("SKUs should only contain letters that we stock.")
            counts[c] += 1
        return counts