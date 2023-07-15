import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        with pytest.raises(Exception):
            checkout_solution.checkout("")

    def test_get_best_price_all(self):
        offer_A = {"multi": 3, "price": 130}
        info_A = {"count": 4, "price": 50, "offer": offer_A}

        offer_B = {"multi": 2, "price": 45}
        info_B = {"count": 5, "price": 30, "offer": offer_B}

        info_C = {"count": 5, "price": 20, "offer": {}}
        info_D = {"count": 5, "price": 15, "offer": {}}

        checkout_info = {
            "A": info_A,
            "B": info_B,
            "C": info_C,
            "D": info_D,
        }

    def test_get_best_price(self):
        info_1 = {"count": 0, "price": 10, "offer": {}}
        assert checkout_solution.get_best_price(info_1) == 0

        info_2 = {"count": 10, "price": 10, "offer": {}}
        assert checkout_solution.get_best_price(info_2) == 100

        info_3 = {"count": 10, "price": 10,
                  "offer": {"multi": 2, "price": 10}}
        assert checkout_solution.get_best_price(info_3) == 50

        info_4 = {"count": 11, "price": 10,
                  "offer": {"multi": 2, "price": 10}}
        assert checkout_solution.get_best_price(info_4) == 60
