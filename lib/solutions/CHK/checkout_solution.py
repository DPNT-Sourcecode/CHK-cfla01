from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


def get_best_price_all(
        counts: Dict[str, int],
        offers: Dict[str, Dict[int, int]]
        ) -> int:
    # Counts is a dictionary of "item": count
    # Offers is a dictionary of "item": offer_info
    # Where offer info is parsed to e.g.
    # 3A for 130 => {"count": 3, "price": 130}
    raise NotImplementedError()
    

def get_best_price(count, offer):


