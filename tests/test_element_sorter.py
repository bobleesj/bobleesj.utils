import pytest


def test_get_custom_labels_from_excel(element_sorter):
    assert element_sorter.label_mapping == {
        2: {"A": ["Fe", "Co", "Ni"], "B": ["Si", "Ga", "Ge"]},
        3: {
            "R": ["Sc", "Y", "La"],
            "M": ["Fe", "Co", "Ni"],
            "X": ["Si", "Ga", "Ge"],
        },
        4: {
            "A": ["Sc", "Y", "La"],
            "B": ["Fe", "Co", "Ni"],
            "C": ["Si", "Ga", "Ge"],
            "D": ["Gd", "Tb", "Dy"],
        },
    }


@pytest.mark.parametrize(
    "elements,expected",
    [
        (["Fe", "Si"], ("Fe", "Si")),
        (["Si", "Fe"], ("Fe", "Si")),
        (["Ge", "Ni"], ("Ni", "Ge")),
        (["Ga", "Co"], ("Co", "Ga")),
    ],
)
def test_get_binary_AB_elements(elements, expected, element_sorter):
    result = element_sorter.sort(elements)
    assert result == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (["Sc", "Fe", "Si"], ("Sc", "Fe", "Si")),
        (["Si", "Fe", "Sc"], ("Sc", "Fe", "Si")),
        (["Fe", "Si", "Sc"], ("Sc", "Fe", "Si")),
    ],
)
def test_get_ternary_RMX_elements(elements, expected, element_sorter):
    result = element_sorter.sort(elements)
    assert result == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (["Gd", "Sc", "Fe", "Si"], ("Sc", "Fe", "Si", "Gd")),
        (["Gd", "Si", "Fe", "Sc"], ("Sc", "Fe", "Si", "Gd")),
        (["Y", "Co", "Ga", "Dy"], ("Y", "Co", "Ga", "Dy")),
    ],
)
def test_get_quaternary_ABCD_elements(elements, expected, element_sorter):
    result = element_sorter.sort(elements)
    assert result == expected
