import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        with pytest.raises(Exception):
            checkout_solution.checkout("")

    def test_get_best_price_all(self):