import numpy as np
import os
from sympy.core import function


def parse_function(expr: str) -> function:
    """
    Parses a math expression and returns a lambda to evaluate it.
    Replaces '^' with '**' and converts to lowercase.
    Only 'log10' and 'sqrt' from numpy are allowed.

    Args:
        expr (str): The expression string.

    Returns:
        function: A lambda that evaluates the expression with 'x'.
    """
    safe_dict = {"log10": np.log10, "sqrt": np.sqrt}

    expr = expr.replace("^", "**").lower()

    return lambda x: eval(expr, {"__builtins__": None}, {**safe_dict, "x": x})


def add_fonts(database):
    """
    Adds all font files from the 'view' directory to the given QFontDatabase.

    Args:
        database (QFontDatabase): The QFontDatabase instance to which the fonts will be added.

    Returns:
        None
    """
    # Get the path to the fonts directory
    fonts_dir = os.path.join(get_project_root(), "src", "view")
    # Get the path to the font files
    for font_file in os.listdir(fonts_dir):
        font_path = os.path.join(fonts_dir, font_file)
        print(font_path)
        database.addApplicationFont(font_path)  # Add the font to the database


def get_project_root():
    """
    Get the project root directory.

    Args:
        None

    Returns:
        str: The full path to the project root directory.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_styles_path():
    """
    Get the full path to styles.qss file.

    Args:
        None

    Returns:
        str: The full path to the styles.qss file.
    """
    return os.path.join(get_project_root(), "src", "view", "styles.qss")
