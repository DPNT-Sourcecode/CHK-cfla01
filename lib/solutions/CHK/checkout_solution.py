from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


def get_best_price(item_count, item_info):
    if not item_info["offer"]:
        return item_info["price"] * item_count

    how_many_offers = item_count // item_info["offer"]["multi"]
    offer_cost = how_many_offers * item_info["offer"]["price"]

    remaining_items = item_count % item_info["offer"]["multi"]
    remaining_cost = remaining_items * item_info["price"]

    return offer_cost + remaining_cost


def get_best_price_all(
        checkout_counts: Dict[str, int],
        checkout_info: Dict[str, Dict],
        ) -> int:
    # checkout_info is a Dict of "item": item_info
    # (item will be e.g. "A")
    # item_info is a dict of 
    # {"price": 50, "offer": offer_info}
    # where offer_info is parsed to e.g.
    # 3A for 130 => {"multi": 3, "price": 130}
    #
    # checkout_counts is a Dict of "item": item_counts
    best_prices = [
        get_best_price 
        for item_name in checkout_counts.keys()
    ]
    raise NotImplementedError()

