import pytest

from openportfoliolabs.returns import apply_return, apply_return_sequence


def test_apply_positive_return() -> None:
    assert apply_return(1_000, 0.05) == 1_050


def test_apply_negative_return() -> None:
    assert apply_return(1_000, -0.10) == 900


def test_apply_return_sequence() -> None:
    result = apply_return_sequence(
        starting_value=1_000,
        return_rates=[0.10, -0.20, 0.05],
    )

    assert result == pytest.approx([1_100, 880, 924])


def test_apply_empty_return_sequence() -> None:
    assert apply_return_sequence(1_000, []) == []
