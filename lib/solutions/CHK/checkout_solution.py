from typing import Dict, Tuple


def chk_r1_info():
    info = {
        (("A", 1)): 50,
        (("A", 3)): 130,
        (("B", 1)): 30,
        (("B", 2)): 45,
        (("C", 1)): 20,
        (("D", 1)): 15,
    }
    return info


def chk_r2_info():
    info = {
        (("A", 1)): 50,
        (("A", 3)): 130,
        (("A", 5)): 200,
        (("B", 1)): 30,
        (("B", 2)): 45,
        (("C", 1)): 20,
        (("D", 1)): 15,
        (("E", 1)): 40,
        (("E", 2), ("B", 1)): 40,
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
        self.best_price_cache = {}

    def get_best_price(
            self,
            item_name: str,
            count: int
            ):
        if item_name not in self.best_price_cache:
            self.best_price_cache[item_name] = {0: 0}
        if count in self.best_price_cache[item_name]:
            return self.best_price_cache[item_name][count]
        running_prices = []
        for multiple in self.price_table[item_name].keys():
            if count >= multiple:
                remaining = self.get_best_price(item_name, count - multiple)
                current = self.price_table[item_name][multiple]
                running_prices.append(remaining + current)
        self.best_price_cache[item_name][count] = min(running_prices)
        return self.best_price_cache[item_name][count]

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
        counts = {name: 0 for name in self.price_table.keys()}
        for c in skus:
            if c not in counts:
                raise ValueError("SKUs should only contain letters that we stock.")
            counts[c] += 1
        return counts

