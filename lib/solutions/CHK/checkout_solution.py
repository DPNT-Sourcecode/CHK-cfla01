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
        # {"price": 50, "offer": offer_info}
        # where offer_info is parsed to e.g.
        # 3A for 130 => {"multi": 3, "price": 130}
        self.price_table = price_table

    def get_best_price(
            self,
            item_name: str,
            count: int
            ):
        item_info = self.price_table[item_name]
        if not item_info["offer"]:
            return item_info["price"] * count

        how_many_offers = count // item_info["offer"]["multi"]
        offer_cost = how_many_offers * item_info["offer"]["price"]

        remaining_items = count % item_info["offer"]["multi"]
        remaining_cost = remaining_items * item_info["price"]

        return offer_cost + remaining_cost

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

