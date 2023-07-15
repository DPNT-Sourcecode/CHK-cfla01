from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


def get_best_price_all(
        total_checkout_info: Dict[str, Dict],
        ) -> int:
    # total_checkout_info is a Dict of "item": item_info
    # where item_info is a dict of 
    # where offer_info is parsed to e.g.
    # 3A for 130 => {"count": 3, "price": 130}
    raise NotImplementedError()
    

def get_best_price(count, offer):
    if 
    



