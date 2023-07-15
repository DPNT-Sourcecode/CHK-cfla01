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


@pytest.fixture
def chk_r3():
    chk_r3 = checkout_solution.Checkout(
        checkout_solution.chk_r3_info()
        )
    return chk_r3


class TestCheckout():
    def test_checkout_r4(self):
        assert checkout_solution.checkout("HHHHHKKNNNM") == 45 + 150 + 120
        assert checkout_solution.checkout("PPPPPQQQQRRR") == 200 + 80 + 150
        assert checkout_solution.checkout("UUUVVV") == 120 + 130
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1880
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("PPPPQRUVPQRUVPQRUVSU") == 740

    def test_checkout_r3(self):
        assert checkout_solution.checkout_r3("AF") == 50 + 10
        assert checkout_solution.checkout_r3("AFF") == 50 + 20
        assert checkout_solution.checkout_r3("AFFF") == 50 + 20
        assert checkout_solution.checkout_r3("AFFFFF") == 50 + 20 + 20
        assert checkout_solution.checkout_r3("AFFFFFF") == 50 + 20 + 20

    def test_checkout_r2(self):
        assert checkout_solution.checkout_r2("AAAAA") == 200
        assert checkout_solution.checkout_r2("AAAAAA") == 250
        assert checkout_solution.checkout_r2("AAAAAAA") == 300
        assert checkout_solution.checkout_r2("EE") == 80
        assert checkout_solution.checkout_r2("EEB") == 80
        assert checkout_solution.checkout_r2("EEEB") == 120

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


