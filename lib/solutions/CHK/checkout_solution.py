from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


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
