from typing import Dict, Tuple


def chk_r1_info():
    offer_A = {"multi": 3, "price": 130}
    info_A = {"price": 50, "offer": [offer_A]}
    offer_B = {"multi": 2, "price": 45}
    info_B = {"price": 30, "offer": [offer_B]}
    info_C = {"count": 5, "price": 20, "offer": {}}
    info_D = {"price": 15, "offer": {}}
    info = {
        "A": info_A,
        "B": info_B,
        "C": info_C,
        "D": info_D,
    }
    return info


def chk_r2_info():
    offer_A1 = {"multi": 3, "price": 130}
    offer_A2 = {"multi": 5, "price": 200}
    info_A = {"price": 50, "offer": [offer_A1, offer_A2]}
    offer_B = {"multi": 2, "price": 45}
    info_B = {"price": 30, "offer": [offer_B]}
    info_C = {"count": 5, "price": 20, "offer": {}}
    info_D = {"price": 15, "offer": {}}
    offer_E = {"multi": 2, "price": 40}
    info_E = {"price": 40, "offer": {}}
    info = {
        "A": info_A,
        "B": info_B,
        "C": info_C,
        "D": info_D,
        "E": info_E,
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
        # price_table is a dictionary of
        # "item_name": item_info
        # (item_name will be e.g. "A")
        # item_info is a dict of 
        # {"price": 50, "offer": List[offer_info]}
        # where offer_info is parsed to e.g.
        # 3A for 130 => {"multi": 3, "price": 130}
        self.price_table = price_table
        self.validate_offers()

    def validate_offers(self):
        # Make sure that all offers are arranged in
        # decreasing item result price (i.e. best offer first)
        offer_lists = {
            item: info["offer"]
            for item, info in self.price_table.items()
        }
        for item, offer_list in offer_lists.items():
            last_price = self.price_table[item]["price"]
            for offer in offer_list:
                offer_price = offer["price"] / offer["multi"]
                if offer_price > last_price:
                    raise ValueError()
                last_price = offer_price

    def get_best_price(
            self,
            item_name: str,
            count: int
            ):
        item_info = self.price_table[item_name]
        if not item_info["offer"]:
            return item_info["price"] * count

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


