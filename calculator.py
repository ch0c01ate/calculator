import numexpr as ne
import re


def calculate(expr):
    try:
        return ne.evaluate(expr).item() if validate_expression(
            expr) else "Invalid expression!"
    except:
        return "Invalid expression!"


def validate_expression(expr):
    return bool(
        re.match(
            r"^\s*[+-]?\s*(?:\d+(?:\.\d*)?|\.\d+)(?:\s*[-+/*^]\s*\s*[+-]?\s*(?:\d+(?:\.\d*)?|\.\d+))*\s*$",
            expr))
