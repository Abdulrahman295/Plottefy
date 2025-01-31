import numpy as np
from src.utils.common import parse_function


class Plotter:
    """A class used to plot two mathematical functions and their intersections."""

    def __init__(self, func1_expr: str, func2_expr: str, intersections: list):
        self.func1_expr = func1_expr
        self.func2_expr = func2_expr
        self.func1 = parse_function(func1_expr)
        self.func2 = parse_function(func2_expr)
        self.intersections = intersections
        self.x_range = self.set_range(func1_expr, func2_expr)
        self.num_points = 2000

    def set_range(self, func1_expr: str, func2_expr: str) -> tuple:
        """
        Auto-adjust x-axis range based on found roots.

        Args:
            func1_expr (str): The expression of the first function.
            func2_expr (str): The expression of the second function.

        Returns:
            tuple: A tuple representing the range (min, max) for plotting.
        """
        if not self.intersections:
            if "log10" in func1_expr.lower() or "log10" in func2_expr.lower():
                return 0.1, 10
            elif "sqrt" in func1_expr.lower() or "sqrt" in func2_expr.lower():
                return 0, 10
            else:
                return -10, 10

        padding = 2
        return (min(self.intersections) - padding, max(self.intersections) + padding)

    def plot(self, ax):
        """
        Plots the functions and their intersections on the given Axes object.

        Args:
            ax (matplotlib.axes.Axes): The axes on which to plot the functions and intersections.

        Returns:
            None
        """
        x = np.linspace(*self.x_range, self.num_points)
        y1 = self.func1(x)
        y2 = self.func2(x)

        ax.plot(x, y1, label=self.func1_expr)
        ax.plot(x, y2, label=self.func2_expr)

        if self.intersections:
            for root in self.intersections:
                y_val = self.func1(root)
                ax.scatter(root, y_val, color="red", s=50, zorder=5)
                ax.annotate(
                    f"({root:.2f}, {y_val:.2f})",
                    (root, y_val),
                    xytext=(15, -15),
                    ha="center",
                    textcoords="offset points",
                )

        ax.set_title("Function Intersections")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.legend()
        ax.axhline(y=0, color="k")
        ax.axvline(x=0, color="k")
