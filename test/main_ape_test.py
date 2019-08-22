import importlib
from unittest import TestCase

from src.main_ape import MainApe
from src.functionrules import FunctionRules


class MainApeTest(TestCase):
    def ape_test_sum(self):
        module = importlib.import_module('src.generated')
        importlib.reload(module)
        gen = getattr(module, 'Gen')
        return gen().sum(1, 2) == 3

    def test_sum(self):
        chunks = ["   ", "+", "a", "b", "return", " "]
        rules = FunctionRules(name="sum"
                              , args="a: int, b: int"
                              , chunks=chunks
                              , minimum_body_size=5
                              , maximum_body_size=6)
        res = MainApe().run(rules, self.ape_test_sum)
        assert len(res) != 0

    def test_diff(self):
        chunks = ["   ", "-", "a", "b", "return", " "]
        rules = FunctionRules(name="sum"
                              , args="a: int, b: int"
                              , chunks=chunks
                              , minimum_body_size=5
                              , maximum_body_size=6)
        res = MainApe().run(rules, self.ape_test_sum)
        assert len(res) != 0
