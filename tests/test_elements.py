from bobleesj.utils.data.elements import Element
import pytest

@pytest.mark.parametrize(
    "element, expected_name, expected_value",
    [
        (Element.H, "H", "Hydrogen"),
        (Element.He, "He", "Helium"),
        (Element.Li, "Li", "Lithium"),
    ]
)
def test_element_enum_names_and_values(element, expected_name, expected_value):
    assert element.name == expected_name
    assert element.value == expected_value

def test_element_enum_length():
    # Test that there are exactly 118 elements
    assert len(Element) == 118

def test_element_enum_values_unique():
    # Test that all enum values are unique
    values = [e.value for e in Element]
    assert len(values) == len(set(values))