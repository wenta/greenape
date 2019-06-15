import importlib

from src.functionrules import FunctionRules
from src.main_ape import MainApe


def ape_test_hello_world():
    module = importlib.import_module('src.generated')
    importlib.reload(module)
    gen = getattr(module, 'Gen')
    return gen().hello() == 'hello world'


def example_hello_world():
    chunks = ["   ", "'", "hello", "world", "return", " "]
    rules = FunctionRules(name="hello"
                          , args=""
                          , chunks=chunks
                          , minimum_body_size=6
                          , maximum_body_size=7)
    print("Generated examples of hello function:")
    MainApe().run(rules, ape_test_hello_world, '../../src/')


if __name__ == '__main__':
    example_hello_world()
