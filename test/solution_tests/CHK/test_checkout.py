import pytest
from solutions.CHK import checkout_solution


@pytest.fixture
def chk_r1():
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

    chk_r1 = checkout_solution.Checkout(info)
    return chk_r1


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("") == 0

    def test_get_best_price_all(self, chk_r1):
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
        assert chk_r1.get_best_price_all(counts) == correct_answer

    def test_get_best_price(self, chk_r1):
        assert chk_r1.get_best_price("A", 0) == 0
        assert chk_r1.get_best_price("A", 2) == 100
        assert chk_r1.get_best_price("A", 3) == 130
        assert chk_r1.get_best_price("A", 4) == 180
