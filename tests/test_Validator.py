import pytest
from src.model.Validator import Validator

@pytest.fixture
def validator():
    return Validator()

def test_validator_init(validator):
    assert "+" in validator.SUPPORTED_OPERATORS
    assert "log10" in validator.SUPPORTED_FUNCTIONS
    assert "x" in validator.SUPPORTED_CHARS
    assert "0" in validator.SUPPORTED_NUMBERS

def test_valid_expressions(validator):
    valid_expressions = [
        "x+1",
        "x^2",
        "log10(x)",
        "sqrt(x)",
        "2*x+1",
        "(x+1)*(x-1)",
        "log10(x)+sqrt(x)",
    ]
    for expr in valid_expressions:
        result = validator.validate_expr(expr)
        assert result["is_valid"], f"Expression '{expr}' should be valid"
        assert len(result["errors"]) == 0

def test_invalid_characters(validator):
    invalid_expressions = [
        "sin(x)",  # unsupported function
        "y+1",  # unsupported variable
        "x#2",  # invalid operator
        "@x",  # invalid character
    ]
    for expr in invalid_expressions:
        result = validator.validate_expr(expr)
        assert not result["is_valid"]
        assert len(result["errors"]) > 0

def test_unbalanced_parentheses(validator):
    invalid_expressions = ["((x+1)", "(x+1))", "((x+1)))", "(x+1"]
    for expr in invalid_expressions:
        result = validator.validate_expr(expr)
        assert not result["is_valid"]
        assert "parentheses" in result["errors"][0].lower()

def test_invalid_sequences(validator):
    invalid_sequences = [
        "x++1",  # consecutive operators
        "+x",  # operator at start
        "x+",  # operator at end
        "x()",  # empty parentheses
        "x y",  # missing operator
    ]
    for expr in invalid_sequences:
        result = validator.validate_expr(expr)
        assert not result["is_valid"]

def test_function_validation(validator):
    invalid_functions = [
        "log10x",  # missing parentheses
        "sqrt",  # incomplete function
        "log10()",  # empty function
        "sqrt(x)log10(x)",  # missing operator between functions
    ]
    for expr in invalid_functions:
        result = validator.validate_expr(expr)
        assert not result["is_valid"]

def test_tokenization(validator):
    expr = "log10(x)+sqrt(2*x)"
    tokens = validator._tokenize_expression(expr)
    expected = ["log10", "(", "x", ")", "+", "sqrt", "(", "2", "*", "x", ")"]
    assert tokens == expected