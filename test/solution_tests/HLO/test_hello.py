from solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello("Ben") == "Hello Ben"
        assert hello_solution.hello("Shirley") == "Hello Shirley"
