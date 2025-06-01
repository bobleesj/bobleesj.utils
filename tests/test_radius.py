import pytest

from bobleesj.utils.sources.radius import get_radius_data, get_radius, get_supported_elements, is_supported


def test_get_radius_data():
    """Test the get_radius_data function."""
    radius_data = get_radius_data()
    
    # Check if the data is a dictionary
    assert isinstance(radius_data, dict)
    
    # Check if it contains expected elements
    expected_elements = ["Li", "Fe", "O", "N"]
    for element in expected_elements:
        assert element in radius_data
    
    # Check if each element has the correct structure
    for element in expected_elements:
        assert isinstance(radius_data[element], dict)
        assert "CIF" in radius_data[element]
        assert "Pauling_CN12" in radius_data[element]

def test_get_radius():
    """Test the get_radius function."""
    assert get_radius("Fe") =={
        'CIF': 1.242,
        'Pauling_CN12': 1.26,
    }
    # Test for an unknown element
    with pytest.raises(KeyError, match="Element 'UnknownElement' not found in radius data."):
        get_radius("UnknownElement")

def test_get_supported_elements():
    """Test the get_supported_elements function."""
    supported_elements = get_supported_elements()
    
    # Check if the result is a list
    assert isinstance(supported_elements, list)
    
    # Check if it contains expected elements
    expected_elements = ["Li", "Fe", "O", "N"]
    for element in expected_elements:
        assert element in supported_elements
    assert len(supported_elements) == 79

def test_is_supported():
    """Test the is_supported function."""
    assert is_supported("Fe") is True
    assert is_supported("UnknownElement") is False
    