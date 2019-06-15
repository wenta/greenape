import importlib

from src.functionrules import FunctionRules
from src.main_ape import MainApe


def ape_test_sum():
    module = importlib.import_module('src.generated')
    importlib.reload(module)
    gen = getattr(module, 'Gen')
    return gen().sum(1, 2) == 3


def ape_test_substract():
    module = importlib.import_module('src.generated')
    importlib.reload(module)
    gen = getattr(module, 'Gen')
    return gen().substract(7, 1) == 6


def ape_test_multiply():
    module = importlib.import_module('src.generated')
    importlib.reload(module)
    gen = getattr(module, 'Gen')
    return gen().multiply(7, 2) == 14


def example_sum():
    chunks = ["   ", "+", "-", "a", "b", "return", " "]
    rules = FunctionRules(name="sum"
                          , args="a: int, b: int"
                          , chunks=chunks
                          , minimum_body_size=5
                          , maximum_body_size=6)
    print("Generated examples of sum function:")
    MainApe().run(rules, ape_test_sum, '../../src/')


def example_substract():
    chunks = ["   ", "+", "-", "a", "b", "return", " "]
    rules = FunctionRules(name="substract"
                          , args="a: int, b: int"
                          , chunks=chunks
                          , minimum_body_size=5
                          , maximum_body_size=6)
    print("Generated examples of substract function:")
    MainApe().run(rules, ape_test_substract, '../../src/')


def example_multiply():
    chunks = ["   ", "*", "a", "b", "return", " "]
    rules = FunctionRules(name="multiply"
                          , args="a: int, b: int"
                          , chunks=chunks
                          , minimum_body_size=5
                          , maximum_body_size=6)
    print("Generated examples of multiply function:")
    MainApe().run(rules, ape_test_multiply, '../../src/')


if __name__ == '__main__':
    example_sum()
    example_substract()
    example_multiply()
