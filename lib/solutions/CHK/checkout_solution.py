from typing import Dict, Tuple


def chk_r1_info():
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    offers = {
        (("A", 3),): 130,
        (("B", 2),): 45,
    }
    return prices, offers


def chk_r2_info():
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    offers = {
        (("A", 3),): 130,
        (("A", 5),): 200,
        (("B", 2),): 45,
        (("E", 2), ("B", 1)): 80,
    }
    return prices, offers


def chk_r3_info():
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }
    offers = {
        (("A", 3),): 130,
        (("A", 5),): 200,
        (("B", 2),): 45,
        (("E", 2), ("B", 1)): 80,
        (("F", 3),): 20,
    }
    return prices, offers


def chk_r4_info():
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }
    offers = {
        (("K", 2),): 150,
        (("H", 5),): 45,
        (("H", 10),): 80,
        (("F", 3),): 20,
        (("B", 2),): 45,
        (("E", 2), ("B", 1)): 80,
        (("N", 3), ("M", 1)): 120,
        (("P", 5),): 200,
        (("Q", 3),): 80,
        (("R", 3), ("Q", 1)): 150,
        (("U", 4),): 120,
        (("V", 2),): 90,
        (("V", 3),): 130,
        (("A", 3),): 130,
        (("A", 5),): 200,
    }
    return prices, offers


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    chk_r4 = Checkout(chk_r4_info())
    try:
        counts = chk_r4.parse_SKUs(skus)
    except ValueError:
        return -1
    return chk_r4.get_best_price_all(counts)


def checkout_r3(skus):
    chk_r3 = Checkout(chk_r3_info())
    try:
        counts = chk_r3.parse_SKUs(skus)
    except ValueError:
        return -1
    return chk_r3.get_best_price_all(counts)


def checkout_r2(skus):
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
        self.best_price_cache = {'{}': 0}

    def get_best_price_all(
            self,
            counts: Dict[str, int]
            ) -> int:

        if str(counts) in self.best_price_cache:
            return self.best_price_cache[str(counts)]

        if max(counts.values()) == 0:
            self.best_price_cache = {str(counts): 0}
            return self.best_price_cache[str(counts)]

        running_prices = []
        for basket_key, basket_price in self.price_table.items():
            basket = self.basket_dicts[basket_key]
            if self.is_subset(basket, counts):
                remainder = self.subtract(basket, counts)
                remainder_price = self.get_best_price_all(remainder)
                running_prices.append(basket_price + remainder_price)
        self.best_price_cache[str(counts)] = min(running_prices)
        return self.best_price_cache[str(counts)]

    def is_subset(self, smaller_set, larger_set):
        for k, v in smaller_set.items():
            if v > larger_set[k]:
                return False
        return True

    def subtract(self, smaller_set, larger_set):
        new_set = {k: v for k, v in larger_set.items()}
        for k, v in smaller_set.items():
            new_set[k] -= v
        return new_set

    def parse_basket_dicts(self):
        self.basket_dicts = {}
        for k in self.price_table.keys():
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


