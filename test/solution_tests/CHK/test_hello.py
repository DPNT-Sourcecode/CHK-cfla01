import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        with pytest.raises(Exception) as e_info:
            checkout_solution.checkout("")
