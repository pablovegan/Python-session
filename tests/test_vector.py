"""We use the @pytest.mark.parametrize decorator to tell the test functions
what inputs to test when we run pytest. This inputs should include the inputs
for function we want to test (for example the __add__ method) as well as the expected result.
"""
import math

import pytest

from my_library import Vector2D


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)
V4 = Vector2D(2, 1)


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
        (V3, V1, Vector2D(2.5, -2.5))
    )
)
def test_add(vector_1: Vector2D, vector_2: Vector2D, result: Vector2D) -> None:
    assert vector_1 + vector_2 == result


@pytest.mark.parametrize(
    ('vector_1', 'vector_2', 'result'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(vector_1: Vector2D, vector_2: Vector2D, result: Vector2D) -> None:
    assert vector_1 * vector_2 == result


@pytest.mark.parametrize(
    ('variable_1', 'variable_2', 'result'),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-2.0, 2.0)),
        (V3, 2.0, Vector2D(5.0, -5.0)),
    )
)
def test_mul_float(variable_1: Vector2D, variable_2: Vector2D, result: float) -> None:
    assert variable_1 * variable_2 == result


@pytest.mark.parametrize(
    ('vector', 'result'),
    (
        (V1, 0),
        (V2, math.sqrt(2)),
        (Vector2D(1, 2), math.sqrt(5))
    )
)
def test_norm(vector: Vector2D, result: float) -> None:
    assert vector.norm == result


@pytest.mark.parametrize(
    ('vector', 'subspace', 'result'),
    (
        (V1, None, Vector2D(0, 0)),
        (V2, None, Vector2D(-1, 0)),
        (V4, Vector2D(1, 1), Vector2D(1.5, 1.5)),
        (V2, Vector2D(1, 1), Vector2D(0, 0))
    )
)
def test_projection(vector: Vector2D, subspace: Vector2D | None, result: Vector2D) -> None:
    assert vector.projection(subspace) == result


@pytest.mark.skip(reason="Not implemented")
def test_whatever_method() -> None:
    pass
