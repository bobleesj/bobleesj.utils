import pytest

from bobleesj.utils.elements import ElementSorter
from bobleesj.utils.sources.oliynyk import Oliynyk


@pytest.fixture
def oliynyk() -> Oliynyk:
    # 20250516 - deleted Tc, Pm and Hg since some properties are not available
    return Oliynyk()


@pytest.fixture
def custom_label_excel_path():
    return "tests/data/sort/test-custom-labels.xlsx"


@pytest.fixture
def custom_labels_from_excel():
    return {
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


@pytest.fixture
def element_sorter(custom_labels_from_excel):
    return ElementSorter(label_mapping=custom_labels_from_excel)
