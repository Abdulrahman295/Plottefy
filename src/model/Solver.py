import numpy as np
from scipy.optimize import brentq
from src.utils.common import parse_function


class Solver:
    """A class used to find the intersections of two mathematical functions."""

    def __init__(self, func1_expr: str, func2_expr: str):
        self.func1 = parse_function(func1_expr)
        self.func2 = parse_function(func2_expr)

    def _fun_diff(self, x):
        """
        Computes the difference between the results of func1 and func2.

        Args:
            self: The Solver instance
            x: The input value to be passed to func1 and func2.

        Returns:
            The difference between the result of func1(x) and func2(x).
        """
        return self.func1(x) - self.func2(x)

    def find_intersections(self) -> dict:
        """
        Finds the intersections (roots) of the derivative of the function within the domain.

        Args:
            self: The Solver instance

        Returns:
            dict: A dictionary with two keys:
                - "error": A string containing the error message if an exception occurs, otherwise an empty string.
                - "intersections": A sorted list of unique roots (intersections).
        """
        # Scan domain for sign changes
        x_values = np.linspace(-100, 100, 1000)
        roots = set()

        # Find intervals with sign changes
        for i in range(len(x_values) - 1):
            a, b = x_values[i], x_values[i + 1]
            try:
                if self._fun_diff(a) * self._fun_diff(b) < 0:  # Sign change detected
                    root = brentq(
                        self._fun_diff, float(a), float(b), xtol=1e-6, rtol=1e-6
                    )
                    roots.add(np.round(root, 6))

            except Exception as e:
                return {"error": str(e), "intersections": []}

        return {"error": "", "intersections": sorted(roots)}
