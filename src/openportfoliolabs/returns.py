from collections.abc import Iterable


def apply_return(starting_value: float, return_rate: float) -> float:
    """Apply a decimal investment return to a portfolio value."""
    return starting_value * (1 + return_rate)


def apply_return_sequence(
    starting_value: float,
    return_rates: Iterable[float],
) -> list[float]:
    """Apply a sequence of decimal returns and return each year-end value."""
    values: list[float] = []
    current_value = starting_value

    for return_rate in return_rates:
        current_value = apply_return(current_value, return_rate)
        values.append(current_value)

    return values
