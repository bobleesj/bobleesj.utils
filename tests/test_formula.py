import pytest

from bobleesj.utils.parsers.formula import Formula

"""
@staticmethod
"""


def test_sort_by_composition():
    formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
    actual_sorted_formula_dict = Formula.sort_by_composition(formulas)
    expected_sorted_formula_dict = {
        2: ["NdSi2", "ThOs"],
        3: ["NdSi2Th2"],
        4: ["YNdThSi2"],
    }
    assert actual_sorted_formula_dict == expected_sorted_formula_dict


def test_get_unique_elements():
    formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
    actual_unique_elements = Formula.get_unique_elements(formulas)
    expected_unique_elements = {"Nd", "Si", "Th", "Os", "Y"}
    assert actual_unique_elements == expected_unique_elements

def test_get_element_count():
    formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
    actual_element_count = Formula.get_element_count(formulas)
    expected_element_count = {
        "Nd": 3,
        "Si": 3,
        "Th": 3,
        "Os": 1,
        "Y": 1,
    }
    assert actual_element_count == expected_element_count

@pytest.mark.parametrize(
    "formula, expected_parsed_formula",
    [
        ("NdSi2", [("Nd", 1), ("Si", 2)]),
        ("Th2Os", [("Th", 2), ("Os", 1)]),
        ("Sm5Co7Sb2", [("Sm", 5), ("Co", 7), ("Sb", 2)]),
        ("SmCoSb", [("Sm", 1), ("Co", 1), ("Sb", 1)]),
        ("ABCD", [("A", 1), ("B", 1), ("C", 1), ("D", 1)]),
        ("A0.1B0.2C0.3D0.4", [("A", 0.1), ("B", 0.2), ("C", 0.3), ("D", 0.4)]),
        ("A1B1C1D1", [("A", 1), ("B", 1), ("C", 1), ("D", 1)]),
    ],
)
def test_parse_formula(formula, expected_parsed_formula):
    actual_parsed_formula = Formula(formula).parsed_formula
    assert actual_parsed_formula == expected_parsed_formula

@pytest.mark.parametrize(
    "parsed_formula, expected_string",
    [
        # Floats with 2 elements
        ([("Nd", 0.333), ("Si", 0.667)], "Nd0.333Si0.667"),
        # Floats with 3 elements
        ([("Sm", 0.25), ("Co", 0.5), ("Sb", 0.25)], "Sm0.25Co0.5Sb0.25"),
        ([("Th", 0.5), ("Os", 0.5)], "Th0.5Os0.5"),
        # Two integers with 2 elements
        ([("A", 1.0), ("B", 1.0)], "AB"),
        # One integer that is 1, expect not to display the integer of 1
        ([("A", 1.0), ("B", 0.5)], "AB0.5"),
        # One integer that is not 1, expect to display the integer
        ([("A", 2.0), ("B", 0.5)], "A2B0.5"),
    ],
)
def test_get_formula_string_from_parsed(parsed_formula, expected_string):
    actual_formula = Formula.build_formula_from_parsed(parsed_formula)
    assert actual_formula == expected_string


@pytest.mark.parametrize(
    "formula, expected",
    [
        ("NdSi2", "Nd0.333333Si0.666667"),
        ("Th2Os", "Th0.666667Os0.333333"),
        ("Sn5Co2", "Sn0.714286Co0.285714"),
        ("ABC", "A0.333333B0.333333C0.333333"),
        ("ABC1", "A0.333333B0.333333C0.333333"),
    ],
)
def test_get_normalized_formula(formula, expected):
    actual = Formula(formula).get_normalized_formula()
    assert actual == expected


@pytest.mark.parametrize(
    "formula, expected",
    [
        ("NdSi2", "Nd0.333Si0.667"),
        ("Th2Os", "Th0.667Os0.333"),
        ("Sn5Co2", "Sn0.714Co0.286"),
        ("ABC", "A0.333B0.333C0.333"),
        ("ABC1", "A0.333B0.333C0.333"),
    ],
)
def test_get_normalized_formula_3_decial(
    formula,
    expected,
):
    actual = Formula(formula).get_normalized_formula(decimals=3)
    assert actual == expected


@pytest.mark.parametrize(
    "formula, expected",
    [
        ("NdSi2", [("Nd", 0.333), ("Si", 0.667)]),
        ("Th2Os", [("Th", 0.667), ("Os", 0.333)]),
    ],
)
def test_normalized_parsed_formula(formula, expected):
    actual = Formula(formula).get_normalized_parsed_formula(decimals=3)
    assert actual == expected


"""
@property
"""


@pytest.mark.parametrize(
    "formula, expected_elements",
    [
        ("NdSi2", ["Nd", "Si"]),
        ("Th2Os", ["Th", "Os"]),
        ("Sm5Co7Sb2", ["Sm", "Co", "Sb"]),
        ("SmCoSb", ["Sm", "Co", "Sb"]),
        ("ABCD", ["A", "B", "C", "D"]),
        ("A1B1C1D1", ["A", "B", "C", "D"]),
    ],
)
def test_get_elements_from_formula(formula, expected_elements):
    actual = Formula(formula).elements
    assert actual == expected_elements


@pytest.mark.parametrize(
    "formula, expected",
    [
        ("NdSi2", 2),  # Binary
        ("Th2Os", 2),  # Binary
        ("Sm5Co7Sb2", 3),  # Ternary
        ("SmCoSb", 3),  # Tenary without numbers
        ("ABCD", 4),  # Quarternary
        ("A1B1C1D1", 4),  # Quarternary
    ],
)
def test_count_element(formula, expected):
    actual = Formula(formula).element_count
    assert actual == expected


@pytest.mark.parametrize(
    "formula, expected_max_min_avg_index",
    [
        ("NdSi2", (2, 1, 1.5)),
        ("Sn5Co2", (5, 2, 3.5)),
        ("NdSi2Th2", (2, 1, 1.667)),
    ],
)
def test_max_min_avg_index(formula, expected_max_min_avg_index):
    actual = Formula(formula).max_min_avg_index
    assert actual == pytest.approx(expected_max_min_avg_index, abs=1e-3)


@pytest.mark.parametrize(
    "formula, expected_indices",
    [
        ("NdSi2", [1.0, 2.0]),
        ("Th2Os", [2.0, 1.0]),
        ("Sm5Co7Sb2", [5.0, 7.0, 2.0]),
        ("SmCoSb", [1.0, 1.0, 1.0]),
        ("ABCD", [1.0, 1.0, 1.0, 1.0]),
        ("A1B1C1D1", [1.0, 1.0, 1.0, 1.0]),
    ],
)
def test_indices(formula, expected_indices):
    actual = Formula(formula).indices
    assert actual == expected_indices


@pytest.mark.parametrize(
    "formula, expected_norm_indices",
    [
        ("NdSi2", [0.333333, 0.666667]),
        ("Th2Os", [0.666667, 0.333333]),
        ("Sm5Co7Sb2", [0.357143, 0.5, 0.142857]),
        ("SmCoSb", [0.333333, 0.333333, 0.333333]),
        ("ABCD", [0.25, 0.25, 0.25, 0.25]),
        ("A1B1C1D1", [0.25, 0.25, 0.25, 0.25]),
    ],
)
def test_get_normalized_indices_from_formula(formula, expected_norm_indices):
    actual = Formula(formula).get_normalized_indices()
    assert actual == expected_norm_indices


