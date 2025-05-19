import re


class Formula:
    def __init__(self, formula: str):
        self.formula = formula
        self.parsed_formula = self._parse_formula(formula)

    @staticmethod
    def sort_by_composition(
        formulas: list[str],
    ) -> dict[int, list[str]]:
        """Sort formulas into categories based on their composition.

        Examples
        --------
        >>> formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
        >>> sort_by_composition(formulas)
        {2: ["NdSi2", "ThOs"], 3: ["NdSi2Th2"], 4: ["YNdThSi2"]}
        """
        sorted_formulas = {}

        for formula in formulas:
            element_count = Formula(formula).element_count
            if element_count not in sorted_formulas:
                sorted_formulas[element_count] = []
            sorted_formulas[element_count].append(formula)
        return sorted_formulas

    @staticmethod
    def count_formulas_by_composition(
        formulas: list[str],
    ) -> dict[int, int]:
        """Count the number of formulas in each composition category.

        Examples
        --------
        >>> formulas = ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"]
        >>> count_formulas_by_composition(formulas)
        {2: 2, 3: 1, 4: 1}
        """
        sorted_formulas = Formula.sort_by_composition(formulas)
        return {k: len(v) for k, v in sorted_formulas.items()}

    @staticmethod
    def get_unique_elements(formulas: list[str]) -> set[str]:
        """Get unique elements from a list of formulas."""
        elements = set()
        for formula in formulas:
            parsed_formula = Formula(formula).parsed_formula
            for element, _ in parsed_formula:
                elements.add(element)
        return elements

    @staticmethod
    def get_element_count(formulas: list[str]) -> dict[str, int]:
        """Get the count of each element in a list of formulas.
        But don't consider the stoichiometry value."""
        element_count = {}
        for formula in formulas:
            parsed_formula = Formula(formula).parsed_formula
            for element, _ in parsed_formula:
                if element not in element_count:
                    element_count[element] = 0
                element_count[element] += 1
        return element_count


    @staticmethod
    def _parse_formula(formula: str) -> list[tuple[str, float]]:
        pattern = r"([A-Z][a-z]*)(\d*\.?\d*)"
        parsed = re.findall(pattern, formula)
        return [
            (element, float(index) if index else 1.0)
            for element, index in parsed
        ]

    @staticmethod
    def build_formula_from_parsed(parsed_formula) -> str:
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
    

    def _normalized(self, decimals: int = 6) -> str:
        index_sum = sum(self.indices)
        normalized = [
            (element, count / index_sum)
            for element, count in self.parsed_formula
        ]
        return "".join(
            f"{element}{format(index, f'.{decimals}f')}"
            for element, index in normalized
        )

    @property
    def elements(self) -> list[str]:
        return [element for element, _ in self.parsed_formula]

    @property
    def indices(self) -> list[float]:
        return [index for _, index in self.parsed_formula]

    @property
    def element_count(self) -> int:
        return len(self.parsed_formula)

    @property
    def max_min_avg_index(self) -> tuple[float, float, float]:
        indices = self.indices
        return max(indices), min(indices), sum(indices) / len(indices)

    def get_normalized_indices(self, decimals=6) -> list[float]:
        total = sum(self.indices)
        return [round(index / total, decimals) for index in self.indices]

    def get_normalized_formula(self, decimals=6) -> str:
        return self._normalized(decimals=decimals)

    def get_normalized_parsed_formula(
        self, decimals=6
    ) -> list[tuple[str, float]]:
        normalized = self._normalized(decimals=decimals)
        return self._parse_formula(normalized)
