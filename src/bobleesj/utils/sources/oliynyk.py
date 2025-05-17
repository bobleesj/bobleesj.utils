import importlib
from enum import Enum

import pandas as pd


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


def get_oliynyk_CAF_data():
    # Load Excel file from the package using importlib.resources
    with importlib.resources.path(
        "bobleesj.utils.data.db", "oliynyk-intermetallics-elements.xlsx"
    ) as path:
        oliynyk_df = pd.read_excel(path)
    # Clean column names: remove spaces
    oliynyk_df.columns = oliynyk_df.columns.str.replace(" ", "", regex=False)
    # Replace NaNs with 0
    oliynyk_df = oliynyk_df.fillna(0)
    # Convert to dictionary keyed by element symbol
    oliynyk_dict = oliynyk_df.set_index("symbol").to_dict(orient="index")
    return oliynyk_dict


def list_supported_elements(db):
    # Get the list of elements in the database
    elements = list(db.keys())
    return elements


def get_property_values(property, db) -> dict[str, float]:
    elements = list_supported_elements(db)
    values = {element: db[element][property] for element in elements}
    print(values)
    return values
