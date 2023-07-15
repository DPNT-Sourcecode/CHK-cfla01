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
            price_table: Dict[Tuple, int]
            ):
        self.price_table = price_table
        self.parse_item_names()
        self.parse_basket_dicts()
        self.best_price_cache = {}

    def get_best_price_all(
            self,
            counts: int
            ) -> int:

        if counts in self.best_price_cache:
            return self.best_price_cache[counts]

        running_prices = []
        for basket_key, basket_price in self.price_table.items():
            basket = self.basket_dicts[basket_key]
            if self.is_subset(basket, counts):
                remainder = self.subtract(basket, counts)
                remainder_price = self.get_best_price_all(remainder)
                running_prices.append(basket_price + remainder_price)
        self.best_price_cache[counts] = min(running_prices)
        return self.best_price_cache[counts]

    def is_subset(self, smaller_set, larger_set):
        for k, v in smaller_set.items():
            if v > larger_set[k]:
                return False
        return True

    def substract(self, smaller_set, larger_set):
        new_set = {k: v for k, v in larger_set.items()}
        for k, v in smaller_set.items():
            new_set[k] -= v
        return new_set

    def parse_basket_dicts(self):
        self.basket_dicts = {}
        for k, _ in self.price_table.keys():
            self.basket_dicts[k] = {name: count for name, count in k}

    def parse_item_names(self):
        self.item_names = set()
        for combination in self.price_table.keys():
            for name, _ in combination:
                self.item_names.add(name)

    def parse_SKUs(self, skus: str) -> Dict[str, int]:
        counts = {name: 0 for name in self.item_names}
        for c in skus:
            if c not in counts:
                raise ValueError("SKUs should only contain letters that we stock.")
            counts[c] += 1
        return counts




