import pytest
from hw01.src.queens_solver import solve_n_queens

def test_n_queens_n4():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2

def test_n_queens_n8():
    solutions = solve_n_queens(8)
    assert len(solutions) == 92

def test_n_queens_n1():
    solutions = solve_n_queens(1)
    assert len(solutions) == 1

def test_n_queens_n0():
    solutions = solve_n_queens(0)
    assert len(solutions) == 1
