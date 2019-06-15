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
    print("Generated example of hello function:")
    MainApe().run(rules, ape_test_hello_world, '../../src/')


def hello():
    return 'hello world'


if __name__ == '__main__':
    print('hello world' == hello())
    example_hello_world()
