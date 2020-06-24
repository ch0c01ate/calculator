import numexpr as ne
import re


def calculate(expr):
    return int(ne.evaluate(expr)) if validate_expression(
        expr) else "Invalid expression!"


def validate_expression(expr):
    return bool(
        re.match(
            r"^\s*[+-]?\s*(?:\d+(?:\.\d*)?|\.\d+)(?:\s*[-+/*^]\s*\s*[+-]?\s*(?:\d+(?:\.\d*)?|\.\d+))*\s*$",
            expr))
