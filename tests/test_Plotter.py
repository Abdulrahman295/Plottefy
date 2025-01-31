import pytest
from matplotlib import pyplot as plt
from src.model.Plotter import Plotter

@pytest.fixture
def plotter():
    func1_expr = "x**2"
    func2_expr = "x**3"
    intersections = [0]
    return Plotter(func1_expr, func2_expr, intersections)

def test_plotter_init(plotter):
    assert plotter.func1_expr == "x**2"
    assert plotter.func2_expr == "x**3"
    assert plotter.intersections == [0]
    assert plotter.x_range == (-2, 2)
    assert plotter.num_points == 2000

def test_set_range_with_negative_intersections():
    plotter = Plotter("x**2", "-x**2", [-1, 1])
    assert plotter.set_range("x**2", "-x**2") == (-3, 3)

def test_set_range_with_large_intersections():
    plotter = Plotter("x**2", "x+10", [-3.162, 3.162])
    assert plotter.set_range("x**2", "x+10") == (-5.162, 5.162)

def test_plot_no_intersections(plotter):
    plotter.intersections = []
    fig, ax = plt.subplots()
    plotter.plot(ax)

    lines = ax.get_lines()
    assert len(lines) == 4

    scatter = ax.collections
    assert len(scatter) == 0

    plt.close(fig)

def test_plot_multiple_intersections():
    plotter = Plotter("x**2-1", "x**3-x", [-1, 0, 1])
    fig, ax = plt.subplots()
    plotter.plot(ax)

    lines = ax.get_lines()
    assert len(lines) == 4

    scatter = ax.collections
    assert len(scatter) == 3

    plt.close(fig)