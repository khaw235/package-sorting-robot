import pytest
from sorter import sort

# Parametrized tests for different scenarios
@pytest.mark.parametrize("dimensions, mass, expected", [
    # Standard packages
    ((10, 20, 30), 5, "STANDARD"),
    ((50, 50, 50), 15, "STANDARD"),  # volume = 125,000
    
    # Bulky by volume
    ((100, 100, 100), 15, "SPECIAL"),  # exact 1,000,000
    ((200, 50, 100), 10, "SPECIAL"),   # volume = 1,000,000
    
    # Bulky by dimension
    ((150, 10, 10), 15, "SPECIAL"),    # exact dimension
    ((10, 160, 10), 15, "SPECIAL"),
    ((10, 10, 170), 15, "SPECIAL"),
    
    # Heavy packages
    ((10, 10, 10), 20, "SPECIAL"),     # exact mass
    ((50, 50, 50), 25, "SPECIAL"),
    
    # Rejected packages
    ((200, 200, 200), 20, "REJECTED"), # bulky + heavy
    ((150, 200, 180), 25, "REJECTED"),
    
    # Edge cases
    ((100, 100, 100), 20, "REJECTED"), # volume 1M + mass 20
    ((150, 10, 10), 20, "REJECTED"),   # dimension 150 + mass 20
])
def test_sort_packages(dimensions, mass, expected):
    width, height, length = dimensions
    assert sort(width, height, length, mass) == expected

# Additional test cases for verification
def test_special_cases():
    # Heavy but not bulky
    assert sort(10, 10, 10, 20) == "SPECIAL"
    
    # Bulky but not heavy (volume)
    assert sort(100, 100, 100, 19) == "SPECIAL"
    
    # Bulky but not heavy (dimension)
    assert sort(150, 10, 10, 19) == "SPECIAL"

def test_corner_cases():
    # Minimum rejected case
    assert sort(150, 150, 150, 20) == "REJECTED"
    
    # Maximum standard package
    assert sort(149, 100, 67, 19) == "STANDARD"