from typing import Dict, Tuple


# WARNING: I am aware that the code is quite fragile.
# You have to manually ensure that the input information is ordered
# such that better offers are listed before worse ones. This is a
# problem for obvious reasons. However, I have already been doing this
# for much too long. In final round I might attempt to fix the problem.
# If you are reading this then I didn't.

def chk_r1_info():
    info = {
        (("A", 1),): 50,
        (("A", 3),): 130,
        (("B", 1),): 30,
        (("B", 2),): 45,
        (("C", 1),): 20,
        (("D", 1),): 15,
    }
    return info


def chk_r2_info():
    info = {
        (("A", 1),): 50,
        (("A", 5),): 200,
        (("A", 3),): 130,
        (("E", 2), ("B", 1)): 80,
        (("B", 1),): 30,
        (("B", 2),): 45,
        (("C", 1),): 20,
        (("D", 1),): 15,
        (("E", 1),): 40,
    }
    return info


def chk_r3_info():
    info = {
        (("A", 1),): 50,
        (("A", 5),): 200,
        (("A", 3),): 130,
        (("E", 2), ("B", 1)): 80,
        (("B", 1),): 30,
        (("B", 2),): 45,
        (("C", 1),): 20,
        (("D", 1),): 15,
        (("E", 1),): 40,
        (("F", 1),): 10,
        (("F", 3),): 20,
    }
    return info


def chk_r4_info():
    info = {
        (("A", 1),): 50,
        (("A", 5),): 200,
        (("A", 3),): 130,
        (("B", 1),): 30,
        (("E", 2), ("B", 1)): 80,
        (("B", 2),): 45,
        (("C", 1),): 20,
        (("D", 1),): 15,
        (("E", 1),): 40,
        (("F", 1),): 10,
        (("F", 3),): 20,
        (("G", 1),): 20,
        (("H", 1),): 10,
        (("H", 10),): 80,
        (("H", 5),): 45,
        (("I", 1),): 35,
        (("J", 1),): 60,
        (("K", 1),): 80,
        (("K", 2),): 150,
        (("L", 1),): 90,
        (("M", 1),): 15,
        (("N", 3), ("M", 1)): 120,
        (("N", 1),): 40,
        (("O", 1),): 10,
        (("P", 1),): 50,
        (("P", 5),): 200,
        (("Q", 1),): 30,
        (("R", 3), ("Q", 1)): 150,
        (("Q", 3),): 80,
        (("R", 1),): 50,
        (("S", 1),): 30,
        (("T", 1),): 20,
        (("U", 1),): 40,
        (("U", 4),): 120,
        (("V", 1),): 50,
        (("V", 3),): 130,
        (("V", 2),): 90,
        (("W", 1),): 20,
        (("X", 1),): 90,
        (("Y", 1),): 10,
        (("Z", 1),): 50,
    }
    return info


def chk_r5_info():
    info = {
        (("A", 1),): 50,
        (("A", 5),): 200,
        (("A", 3),): 130,
        (("B", 1),): 30,
        (("E", 2), ("B", 1)): 80,
        (("B", 2),): 45,
        (("C", 1),): 20,
        (("D", 1),): 15,
        (("E", 1),): 40,
        (("F", 1),): 10,
        (("F", 3),): 20,
        (("G", 1),): 20,
        (("H", 1),): 10,
        (("H", 10),): 80,
        (("H", 5),): 45,
        (("I", 1),): 35,
        (("J", 1),): 60,
        (("K", 1),): 70,
        (("K", 2),): 120,
        (("L", 1),): 90,
        (("M", 1),): 15,
        (("N", 3), ("M", 1)): 120,
        (("N", 1),): 40,
        (("O", 1),): 10,
        (("P", 1),): 50,
        (("P", 5),): 200,
        (("Q", 1),): 30,
        (("R", 3), ("Q", 1)): 150,
        (("Q", 3),): 80,
        (("R", 1),): 50,
        (("U", 1),): 40,
        (("U", 4),): 120,
        (("V", 1),): 50,
        (("V", 3),): 130,
        (("V", 2),): 90,
        (("W", 1),): 20,
    }
    return info


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    chk_r5 = Checkout(chk_r5_info(), special_prices_enable=True)
    try:
        counts = chk_r5.parse_SKUs(skus)
    except ValueError:
        return -1
    return chk_r5.get_best_price_all(counts)


def checkout_r4(skus):
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
            price_table: Dict[Tuple, int],
            special_prices_enable=False
            ):
        self.price_table = price_table
        self.parse_item_names_and_offers()
        self.parse_basket_dicts()
        self.best_price_cache = {'{}': 0}
        self.special_prices_enable = special_prices_enable
        if special_prices_enable:
            self.special_prices = {
                "Z": 21,
                "S": 20,
                "T": 20,
                "Y": 20,
                "X": 17,
            }

    def get_best_price_all(
            self,
            counts: Dict[str, int]
            ) -> int:
            
        if self.special_prices_enable:
            self.special_counts = {}
            for k in self.special_prices.keys():
                self.special_counts[k] = counts[k]
                counts[k] = 0

        # Optimise by pre-counting and subtracting offers afterwards
        price = sum([counts[k] * self.basic_prices[k] for k in counts.keys()])
        for offer_key, offer_price in self.offer_prices.items():
            savings = self.offer_basic_price(offer_key) - offer_price
            offer_multiplier = 0
            while self.is_subset(self.basket_dicts[offer_key], counts):
                offer_multiplier += 1
                counts = self.subtract(self.basket_dicts[offer_key], counts)
            price -= offer_multiplier * savings
        return price + self.special_best_price()

    def special_best_price(self):
        if not self.special_prices_enable:
            return 0
        counter = sum(self.special_counts.values())
        remainder = counter % 3
        counter -= remainder
        buy3value = (counter // 3) * 45
        for k in self.special_counts.keys():
            if self.special_counts[k] <= counter:
                counter -= self.special_counts[k]


    def offer_basic_price(self, offer_key):
        counts = self.basket_dicts[offer_key]
        return sum([counts[k] * self.basic_prices[k] for k in counts.keys()])

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

    def parse_item_names_and_offers(self):
        self.item_names = set()
        self.has_offers = set()
        self.basic_prices = {}
        self.offer_prices = {}
        for combination, price in self.price_table.items():
            # Sort into offers and basic prices
            # I probably should have kept the original input structure
            if len(combination) == 1 and combination[0][1] == 1:
                self.basic_prices[combination[0][0]] = price
            else:
                self.offer_prices[combination] = price
            for name, _ in combination:
                if name in self.item_names:
                    self.has_offers.add(name)
                self.item_names.add(name)

    def parse_SKUs(self, skus: str) -> Dict[str, int]:
        counts = {name: 0 for name in self.item_names}
        for c in skus:
            if c not in counts:
                raise ValueError("SKUs should only contain letters that we stock.")
            counts[c] += 1
        return counts




