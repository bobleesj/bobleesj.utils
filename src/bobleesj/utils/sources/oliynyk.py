import importlib
from enum import Enum

import pandas as pd

from bobleesj.utils.parsers.formula import Formula


class Property(str, Enum):
    AW = "atomic_weight"
    ATOMIC_NUMBER = "atomic_number"
    PERIOD = "period"
    GROUP = "group"
    MEND_NUM = "Mendeleev_number"
    VAL_TOTAL = "valencee_total"
    UNPARIED_E = "unpaired_electrons"
    GILMAN = "Gilman"
    Z_EFF = "Z_eff"
    ION_ENERGY = "ionization_energy"
    COORD_NUM = "coordination_number"
    RATIO_CLOSEST = "ratio_closest"
    POLYHEDRON_DISTORT = "polyhedron_distortion"
    CIF_RADIUS = "CIF_radius"
    PAULING_RADIUS_CN12 = "Pauling_radius_CN12"
    PAULING_EN = "Pauling_EN"
    MARTYNOV_BATSANOV_EN = "Martynov_Batsanov_EN"
    MELTING_POINT_K = "melting_point_K"
    DENSITY = "density"
    SPECIFIC_HEAT = "specific_heat"
    COHESIVE_ENERGY = "cohesive_energy"
    BULK_MODULUS = "bulk_modulus"

    @classmethod
    def display(cls):
        print("\nAvailable elemental properties:")
        for index, prop in enumerate(cls, start=1):
            print(f"  {index}. {prop.name} - {prop.value}")

    @classmethod
    def select(cls):
        cls.display()
        try:
            choice = int(input("\nEnter the number of the property to use: "))
            selected = list(cls)[choice - 1]
            print(f"\nYou selected: {selected.name} → {selected.value}")
            return selected
        except (IndexError, ValueError):
            print("Invalid choice. Please enter a valid number.")
            return None


class Oliynyk:
    """Oliynyk elemental property database interface.

    Examples
    --------
    from bobleesj.utils.sources.oliynyk import Property as P
    >>> oliynyk = Oliynyk()
    >>> oliynyk.is_formula_supported("LiFePO4")
    True
    >>> oliynyk.get_property_data(P.AW)["Fe"]
    55.845
    """

    def __init__(self):
        self.db = self.get_oliynyk_CAF_data()
        self.elements = self.list_supported_elements()

    def get_oliynyk_CAF_data(self):
        with importlib.resources.path(
            "bobleesj.utils.data.db", "oliynyk-elemental-property-list.xlsx"
        ) as path:
            oliynyk_df = pd.read_excel(path)
        oliynyk_df.columns = oliynyk_df.columns.str.replace(
            " ", "", regex=False
        )
        oliynyk_df = oliynyk_df.fillna(0)
        oliynyk_dict = oliynyk_df.set_index("symbol").to_dict(orient="index")
        return oliynyk_dict

    def list_supported_elements(self) -> list[str]:
        """List all elements in the Oliynyk database."""
        return list(self.db.keys())

    def get_property_data(self, property: Property) -> dict[str, float]:
        return {
            element: self.db[element][property] for element in self.elements
        }

    def get_property_data_for_formula(
        self, formula: str, property: Property
    ) -> dict[str, float]:
        """Get property data for elements in a given formula.

        Examples
        --------
        >>> oliynyk.get_property_data_for_formula("LiFePO4", Property.AW)
        {'Li': 6.941, 'Fe': 55.845, 'P': 30.973761, 'O': 15.999}
        """
        elements = Formula(formula).elements
        return {element: self.db[element][property] for element in elements}

    def is_formula_supported(self, formula: str) -> bool:
        """Check if a formula is supported by the Oliynyk database.

        Examples
        --------
        >>> oliynyk.is_formula_supported("LiFePO4")
        True
        >>> oliynyk.is_formula_supported("FeH")
        False
        """
        elements_parsed = Formula(formula).elements
        return all(element in self.elements for element in elements_parsed)

    def get_supported_formulas(
        self, formulas: list[str]
    ) -> tuple[list[str], list[str]]:
        """Filter formulas to only include those with supported elements.

        Examples
        --------
        >>> formulas = ["LiFePO4", "FeH", "NdSi2"]
        >>> supported, unsupported = oliynyk.filter_supported_formulas(formulas)
        >>> supported
        ['LiFePO4', 'NdSi2']
        >>> unsupported
        ['FeH']
        """
        supported, unsupported = [], []
        for formula in formulas:
            if self.is_formula_supported(formula):
                supported.append(formula)
            else:
                unsupported.append(formula)
        return supported, unsupported
