import pytest

from library.library import fine_tier

# Lab 6 - Boundary Value Analysis for fine_tier(days_overdue)
# Cut-offs: 0 (domain edge), 1, 8, 15, 31


@pytest.mark.parametrize('days,expected', [
    # Domain edge / None -> Low  (0/1)
    (0, 'None'), (1, 'Low'), (2, 'Low'),
    # Low -> Medium  (7/8)
    (7, 'Low'), (8, 'Medium'), (9, 'Medium'),
    # Medium -> High  (14/15)
    (14, 'Medium'), (15, 'High'), (16, 'High'),
    # High -> Severe  (30/31)
    (30, 'High'), (31, 'Severe'), (32, 'Severe'),
])
def test_fine_tier_boundaries(days, expected):
    assert fine_tier(days) == expected


def test_fine_tier_just_below_domain_raises():
    """-1 is one below the lowest valid value (0)."""
    with pytest.raises(ValueError):
        fine_tier(-1)


# Worked example from the lab manual: boundary around the Medium/High cut-off
@pytest.mark.parametrize('days,expected', [
    (14, 'Medium'), (15, 'High'), (16, 'High'),
])
def test_fine_tier_boundary_15(days, expected):
    assert fine_tier(days) == expected

    # Values immediately next to the cut-offs (0/1, 7/8, 14/15, 30/31).
# days_overdue must be a whole number, so fractions must be rejected.
@pytest.mark.parametrize('days', [0.5, 0.99, 7.5, 14.5, 30.5])
def test_fine_tier_fractional_days_rejected(days):
    with pytest.raises(TypeError):
        fine_tier(days)