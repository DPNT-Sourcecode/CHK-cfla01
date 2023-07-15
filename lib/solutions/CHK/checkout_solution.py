from typing import Dict, Tuple


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


def get_best_price_all(
        counts: Dict[str, int],
        offers: Dict[str, Tuple[int, int]]
        ) -> int:
    # Counts is a dictionary of "item": count
    # Offers is a dictionary of "item": offer_price
    # Where offer ratio is e.g. (1, 2) if we get 2-for-1
    raise NotImplementedError()
    

def get_best_price(count, offer):
