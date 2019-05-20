import itertools
import types

from src.functionrules import FunctionRules
from src.utils.files import Files


class MainApe:
    def run(self, rules: FunctionRules, ape_function: types.FunctionType):

        correct_solutions = []

        for i in range(rules.minSize, rules.maxSize):
            xs = [p for p in itertools.product(rules.chunks, repeat=i)]
            for x in xs:
                generated_code = " ".join(x)
                body: str = self.getBody(generated_code, rules)

                Files().save('../src/generated.py', body)

                try:
                    if ape_function() is True:
                        correct_solutions.append(body)
                        print(body)
                except SyntaxError:
                    pass
                except Exception:
                    pass
        return correct_solutions

    def getBody(self, code: str, rules: FunctionRules) -> str:
        return """class Gen:
            def %s(self, %s) -> int:              
                %s\n
        """ % (rules.name, rules.args, code)
