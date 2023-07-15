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
    
