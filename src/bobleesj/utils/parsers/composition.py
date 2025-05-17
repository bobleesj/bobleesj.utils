# Parse the formula
import re


def get_parsed_formula(formula: str) -> list[tuple[str, float]]:
    """Parse it into a list of elements and their indices.

    Examples
    --------
    Get the parsed formula from the formula string:
    >>> get_parsed_formula("NdSi2")
    [('Nd', '1'), ('Si', '2')]
    """
    pattern = r"([A-Z][a-z]*)(\d*\.?\d*)"
    parsed_formula = re.findall(pattern, formula)
    # Replace empty indices with 1.0, the index needs to be a float.
    parsed_formula = [
        (element, float(index) if index else 1.0)
        for element, index in parsed_formula
    ]
    return parsed_formula


def get_normalized_formula(formula: str, decimal_places: int = 6) -> str:
    """Get the normalized formula with the sum of indices equal to 1.

    Example
    """
    parsed_formula = get_parsed_formula(formula)
    index_sum = sum(float(index) for _, index in parsed_formula)
    return "".join(
        f"{element}{float(count) / index_sum:.{decimal_places}f}"
        for element, count in parsed_formula
    )


def get_normalized_parsed_formula(
    formula: str, decimal_places: int = 6
) -> list[tuple[str, str]]:
    """Convert the formula into a list of elements and irnormalized indices."""
    normalized_formula = get_normalized_formula(formula, decimal_places)
    return get_parsed_formula(normalized_formula)


def count_element(formula: str) -> int:
    """Count the number of unique elements in the formula."""
    elements = get_parsed_formula(formula)
    return len(elements)


def get_max_min_avg_index(formula: str) -> tuple[float, float, float]:
    """Get the max, min, and avg index of the formula."""
    parsed_formula = get_parsed_formula(formula)
    indices = [float(index) for _, index in parsed_formula]
    return max(indices), min(indices), sum(indices) / len(indices)


def get_elements_from_formula(formula: str) -> list[str]:
    """Get the elements from the formula."""
    parsed_formula = get_parsed_formula(formula)
    return [element for element, _ in parsed_formula]


def get_indices_from_formula(formula: str) -> list[float]:
    """Get the indices from the formula."""
    parsed_formula = get_parsed_formula(formula)
    return [float(index) for _, index in parsed_formula]


def get_normalized_indices_from_formula(formula: str) -> list[float]:
    """Get the normalized indices from the formula."""
    parsed_formula = get_normalized_parsed_formula(formula)
    return [float(index) for _, index in parsed_formula]


def sort_formulas_by_composition(formulas: list[str]) -> dict[int, list[str]]:
    """Sort formulas into categories based on their composition.

    Examples
    --------
    >>> formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
    >>> sort_formulas_by_composition(formulas)
    {2: ["NdSi2", "ThOs"], 3: ["NdSi2Th2"], 4: ["YNdThSi2"]}
    """
    sorted_formulas = {}

    for formula in formulas:
        element_count = count_element(formula)
        if element_count not in sorted_formulas:
            sorted_formulas[element_count] = []
        sorted_formulas[element_count].append(formula)
    return sorted_formulas

def get_formula_string_from_parsed(parsed_formula: list[tuple[str, float]]) -> str:
    """Convert the parsed formula into a string."""
    formula_string = ""
    for element, index in parsed_formula:
        if index.is_integer() and int(index) != 1:
            formula_string += f"{element}{int(index)}"
        elif index.is_integer() and int(index) == 1:
            formula_string += f"{element}"
        else:
            formula_string += f"{element}{index}"
    return formula_string