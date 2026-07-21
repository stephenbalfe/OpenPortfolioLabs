from openportfoliolabs.returns import apply_return


def test_apply_positive_return() -> None:
    assert apply_return(1_000, 0.05) == 1_050


def test_apply_negative_return() -> None:
    assert apply_return(1_000, -0.10) == 900
