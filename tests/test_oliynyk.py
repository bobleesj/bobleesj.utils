import pytest

from bobleesj.utils.sources.oliynyk import Property as P
from bobleesj.utils.sources.oliynyk import (
    check_formula_in_oliynyk,
    get_oliynyk_CAF_data,
    get_property_values,
    list_supported_elements,
)


@pytest.mark.parametrize(
    "property, expected_string",
    [
        (P.AW, "atomic_weight"),
        (P.ATOMIC_NUMBER, "atomic_number"),
        (P.GROUP, "group"),
        (P.PERIOD, "period"),
        (P.MEND_NUM, "Mendeleev_number"),
        (P.VAL_TOTAL, "valencee_total"),
        (P.UNPARIED_E, "unpaired_electrons"),
        (P.GILMAN, "Gilman"),
        (P.Z_EFF, "Z_eff"),
        (P.ION_ENERGY, "ionization_energy"),
        (P.COORD_NUM, "coordination_number"),
        (P.RATIO_CLOSEST, "ratio_closest"),
        (P.POLYHEDRON_DISTORT, "polyhedron_distortion"),
        (P.CIF_RADIUS, "CIF_radius"),
        (P.PAULING_RADIUS_CN12, "Pauling_radius_CN12"),
        (P.PAULING_EN, "Pauling_EN"),
        (P.MARTYNOV_BATSANOV_EN, "Martynov_Batsanov_EN"),
        (P.MELTING_POINT_K, "melting_point_K"),
        (P.DENSITY, "density"),
        (P.SPECIFIC_HEAT, "specific_heat"),
        (P.COHESIVE_ENERGY, "cohesive_energy"),
        (P.BULK_MODULUS, "bulk_modulus"),
    ],
)
def test_property(property, expected_string):
    assert property == expected_string


def test_get_oliynyk_CAF_data():
    db = get_oliynyk_CAF_data()
    # Number of elements in the database
    assert len(db) == 33
    assert db["Nd"]["atomic_weight"] == 144.242
    assert db["Nd"]["atomic_number"] == 60


def test_list_supported_elements(CAF_oliynyk_db):
    actual_elements = list_supported_elements(CAF_oliynyk_db)
    expected_elements = [
        "Si",
        "Sc",
        "Fe",
        "Co",
        "Ni",
        "Ga",
        "Ge",
        "Y",
        "Ru",
        "Rh",
        "Pd",
        "In",
        "Sn",
        "Sb",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Os",
        "Ir",
        "Pt",
        "Th",
        "U",
    ]
    assert actual_elements == expected_elements


def test_get_property_values(CAF_oliynyk_db):
    actual_values = get_property_values(P.AW, CAF_oliynyk_db)
    expected_values = {
        "Si": 28.0855,
        "Sc": 44.95591,
        "Fe": 55.847,
        "Co": 58.9332,
        "Ni": 58.6934,
        "Ga": 69.723,
        "Ge": 72.63,
        "Y": 88.90584,
        "Ru": 101.07,
        "Rh": 102.9055,
        "Pd": 106.42,
        "In": 114.818,
        "Sn": 118.71,
        "Sb": 121.76,
        "La": 138.9055,
        "Ce": 140.115,
        "Pr": 140.90765,
        "Nd": 144.242,
        "Sm": 150.36,
        "Eu": 151.965,
        "Gd": 157.25,
        "Tb": 158.92534,
        "Dy": 162.5,
        "Ho": 164.93032,
        "Er": 167.259,
        "Tm": 168.93421,
        "Yb": 173.045,
        "Lu": 174.967,
        "Os": 190.23,
        "Ir": 192.217,
        "Pt": 195.084,
        "Th": 232.0381,
        "U": 238.0289,
    }
    assert actual_values == expected_values


@pytest.mark.parametrize(
    "formula, expected_result",
    [
        ("NdSi2", True),
        ("XYZ", False),
        ("FeCo", True),
        ("FeH", False),
        ("SiGe", True),
        ("ABCD", False),
        ("LaNi5", True),
        ("UTh", True),
        ("Invalid123", False),
        ("PtIr", True),
    ],
)
def test_check_formula_in_oliynyk(formula, expected_result, CAF_oliynyk_db):
    elements_supported = list_supported_elements(CAF_oliynyk_db)
    assert (
        check_formula_in_oliynyk(formula, elements_supported)
        == expected_result
    )
