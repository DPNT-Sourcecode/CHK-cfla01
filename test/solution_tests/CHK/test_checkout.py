import pytest
from solutions.CHK import checkout_solution


@pytest.fixture
def chk_r1():
    chk_r1 = checkout_solution.Checkout(
        checkout_solution.chk_r1_info()
        )
    return chk_r1


@pytest.fixture
def chk_r2():
    chk_r2 = checkout_solution.Checkout(
        checkout_solution.chk_r2_info()
        )
    return chk_r2


class TestCheckout():
    def test_checkout_r2(self):
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_checkout_r1(self):
        assert checkout_solution.checkout_r1("ABxD") == -1
        assert checkout_solution.checkout_r1("AAAABBBBBCCCCCDDDDD") == 475

    def test_parse_SKUs(self, chk_r1):
        assert chk_r1.parse_SKUs("") == {
            "A": 0, "B": 0, "C": 0, "D": 0
            }
        assert chk_r1.parse_SKUs("A") == {
            "A": 1, "B": 0, "C": 0, "D": 0
            }
        assert chk_r1.parse_SKUs("ABCD") == {
            "A": 1, "B": 1, "C": 1, "D": 1
            }
        with pytest.raises(ValueError):
            chk_r1.parse_SKUs("ABxD")

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
