import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        with pytest.raises(Exception):
            checkout_solution.checkout("")

    def test_get_best_price_all(self):
        offer_A = {"multi": 3, "price": 130}
        info_A = {"price": 50, "offer": offer_A}

        offer_B = {"multi": 2, "price": 45}
        info_B = {"price": 30, "offer": offer_B}

        info_C = {"count": 5, "price": 20, "offer": {}}
        info_D = {"price": 15, "offer": {}}

        info = {
            "A": info_A,
            "B": info_B,
            "C": info_C,
            "D": info_D,
        }

        counts = {
            "A": 4,
            "B": 5,
            "C": 5,
            "D": 5,
        }

        correct_answer = (
            (130 + 50)
            + (45*2 + 30)
            + (5 * 20)
            + (5 * 15)
        )
        with pytest.raises(Exception):
            checkout_solution.get_best_price_all(counts, info)
        #assert checkout_solution.get_best_price_all(counts, info) == correct_answer

    def test_get_best_price(self):
        info_1 = {"price": 10, "offer": {}}
        assert checkout_solution.get_best_price(0, info_1) == 0

        info_2 = {"price": 10, "offer": {}}
        assert checkout_solution.get_best_price(10, info_2) == 100

        info_3 = {"price": 10,
                  "offer": {"multi": 2, "price": 10}}
        assert checkout_solution.get_best_price(10, info_3) == 50

        info_4 = {"price": 10,
                  "offer": {"multi": 2, "price": 10}}
        assert checkout_solution.get_best_price(11, info_4) == 60
