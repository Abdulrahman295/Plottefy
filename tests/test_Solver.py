import pytest
import numpy as np
from src.model.Solver import Solver

@pytest.fixture
def solver():
    return Solver("x**2", "x")

def test_solver_init(solver):
    assert callable(solver.func1)
    assert callable(solver.func2)

def test_simple_intersection():
    solver = Solver("x**2", "x")
    result = solver.find_intersections()
    assert result["error"] == ""
    assert len(result["intersections"]) == 2
    assert np.isclose(result["intersections"][0], 0)
    assert np.isclose(result["intersections"][1], 1)

def test_no_intersections():
    solver = Solver("x**2 + 1", "0")
    result = solver.find_intersections()
    assert result["error"] == ""
    assert len(result["intersections"]) == 0

def test_invalid_function():
    solver = Solver("invalid", "x")
    result = solver.find_intersections()
    assert result["error"] != ""
    assert len(result["intersections"]) == 0

def test_log_intersection():
    solver = Solver("log10(x)", "0")
    result = solver.find_intersections()
    assert result["error"] == ""
    assert len(result["intersections"]) == 1
    assert np.isclose(result["intersections"][0], 1)

def test_sqrt_intersection():
    solver = Solver("sqrt(x)", "x-2")
    result = solver.find_intersections()
    assert result["error"] == ""
    assert len(result["intersections"]) == 1
    assert np.isclose(result["intersections"][0], 4)

def test_combined_functions():
    solver = Solver("sqrt(x) + log10(x)", "x")
    result = solver.find_intersections()
    assert result["error"] == ""
    assert len(result["intersections"]) >= 1

def test_fun_diff():
    solver = Solver("x**2", "x")
    assert np.isclose(solver._fun_diff(2), 2)
    assert np.isclose(solver._fun_diff(0), 0)