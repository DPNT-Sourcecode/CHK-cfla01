import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        with pytest.raises(Exception):
            checkout_solution.checkout("")

    def test_get_best_price_all(self):

    def test_get_best_price_all(self):
        info_1 = {"count": 0, "price": 10, "offer": {}}
        assert checkout_solution.get_best_price(info_1) == 0
        info_2 = {"count": 10, "price": 10, "offer": {}}
        assert checkout_solution.get_best_price(info_2) == 100
        info_2 = {"count": 10, "price": 10,
                  "offer": {"multi": 2, "price": 10}}
        assert checkout_solution.get_best_price(info_3) == 50