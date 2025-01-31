import re


class Validator:
    """Class responsible for validating function expressions."""

    def __init__(self):
        self.SUPPORTED_OPERATORS = ["+", "-", "*", "/", "^"]
        self.SUPPORTED_FUNCTIONS = ["log10", "sqrt"]
        self.SUPPORTED_CHARS = ["x", "X"]
        self.SUPPORTED_NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def validate_expr(self, expr: str) -> dict:
        """
        Validates a given function expression.

        Args:
            expr (str): The function expression to validate.

        Returns:
            dict: A dictionary with two keys:
            - "is_valid" (bool): True if the expression is valid, False otherwise.
            - "errors" (list): A list of error messages if the expression is invalid.
        """
        tokens = self._tokenize_expression(expr)
        validations = [
            self._contains_unsupported_chars(tokens),
            self._is_unbalanced_parentheses(tokens),
            self._is_invalid_sequence(tokens),
        ]
        errors = [result[1] for result in validations if result[0]]
        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
        }

    def _tokenize_expression(self, expr: str) -> list:
        """
        Tokenizes a mathematical expression into its constituent parts.

        Args:
            expr (str): The mathematical expression to tokenize.

        Returns:
            list: A list of tokens extracted from the expression.
        """
        # token_pattern = re.compile(r"log10|sqrt|[xX]|\d+(?:\.\d+)?|[+\-*/^()]")
        token_pattern = re.compile(
            r"log10|sqrt|[xX]|\d+(?:\.\d+)?|[+\-*/^()]|[a-zA-Z]+|[^\s\w\d+\-*/^()]"
        )
        return token_pattern.findall(expr)

    def _contains_unsupported_chars(self, tokens: list) -> (bool, str):
        """
        Validates tokens for unsupported characters.

        Args:
            tokens (list): Tokens to validate.

        Returns:
            tuple (bool, str): indicating if an unsupported character is found and the error message.
        """
        for token in tokens:
            if (
                token
                not in self.SUPPORTED_OPERATORS
                + self.SUPPORTED_FUNCTIONS
                + self.SUPPORTED_CHARS
                + ["(", ")"]
                and not re.match(r"\d+(?:\.\d+)?", token)
            ):
                return True, "Invalid character: " + token

        return False, ""

    def _is_unbalanced_parentheses(self, tokens: list) -> (bool, str):
        """
        Checks if the given list of tokens contains unbalanced parentheses.

        Args:
            tokens (list): A list of tokens (strings) to be checked for balanced parentheses.

        Returns:
            tuple (bool, str): indicating if unbalanced parentheses are found and the error message.
        """
        stack = []
        for token in tokens:
            if token == "(":
                stack.append(token)
            elif token == ")":
                if not stack:
                    return True, "Unbalanced parentheses: too many closing parentheses"
                stack.pop()

        if stack:
            return True, "Unbalanced parentheses: too many opening parentheses"

        return False, ""

    def _is_invalid_sequence(self, tokens: list) -> (bool, str):
        """
        Validates a sequence of tokens to ensure they form a valid expression.

        Args:
            tokens (list): A list of tokens representing parts of an expression.

        Returns:
            tuple (bool, str): indicating if an invalid sequence is found and the error message.
        """
        for i, curr in enumerate(tokens):
            prev = tokens[i - 1] if i > 0 else None
            nxt = tokens[i + 1] if i < len(tokens) - 1 else None

            if curr in self.SUPPORTED_OPERATORS:
                if not prev or not nxt:
                    return (
                        True,
                        f"Operator '{curr}' cannot be at the start or end of the expression",
                    )

                if nxt in self.SUPPORTED_OPERATORS:
                    return True, f"Cannot have consecutive operators: '{curr}{nxt}'"

            elif curr in self.SUPPORTED_CHARS:
                if prev and prev not in self.SUPPORTED_OPERATORS + ["("]:
                    return (
                        True,
                        f"Variable '{curr}' must be preceded by an operator or opening parenthesis, not '{prev}'",
                    )

                if nxt and nxt not in self.SUPPORTED_OPERATORS + [")"]:
                    return (
                        True,
                        f"Variable '{curr}' must be followed by an operator or closing parenthesis, not '{nxt}'",
                    )

            elif curr in self.SUPPORTED_FUNCTIONS:
                if nxt != "(":
                    return (
                        True,
                        f"Function '{curr}' must be immediately followed by an opening parenthesis",
                    )

                if prev and prev not in self.SUPPORTED_OPERATORS + ["("]:
                    return (
                        True,
                        f"Function '{curr}' must be preceded by an operator, not '{prev}'",
                    )

            elif curr == "(":
                if not nxt:
                    return True, "Opening parenthesis cannot be the last token"
                if nxt == ")":
                    return True, "Empty parentheses are not allowed"

                if prev and prev == ")":
                    return (
                        True,
                        f"Cannot place opening parenthesis '{curr}' directly after closing parenthesis '{prev}'",
                    )

            elif curr == ")":
                if not prev:
                    return True, "Closing parenthesis cannot be the first token"

            else:
                if prev and prev not in self.SUPPORTED_OPERATORS + ["("]:
                    return (
                        True,
                        f"Number '{curr}' must be preceded by an operator or opening parenthesis, not '{prev}'",
                    )

                if nxt and nxt not in self.SUPPORTED_OPERATORS + [")"]:
                    return (
                        True,
                        f"Number '{curr}' must be followed by an operator or closing parenthesis, not '{nxt}'",
                    )

        return False, ""