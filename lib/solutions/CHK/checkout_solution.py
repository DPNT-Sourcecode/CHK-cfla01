from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


def get_best_price_all(
        total_checkout_info: Dict[str, Dict],
        ) -> int:
    # total_checkout_info is a Dict of "item": item_info
    # (item will be e.g. "A")
    # item_info is a dict of 
    # {"count": 20, "price": 50, "offer": offer_info}
    # where offer_info is parsed to e.g.
    # 3A for 130 => {"multi": 3, "price": 130}
    raise NotImplementedError()
    

def get_best_price(item_info):
    if not item_info["offer"]:
        return item_info["price"] * item_info["count"]
    

