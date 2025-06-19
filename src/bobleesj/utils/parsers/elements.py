import pandas as pd


def get_custom_labels_from_excel(excel_path: str) -> dict:
    """Read custom labels from an Excel file and return a dictionary
    mapping.

    This function is used in SAF and CAF applciations.
    """

    sheet_map = {
        2: ("Binary", ["Element_A", "Element_B"]),
        3: ("Ternary", ["Element_R", "Element_M", "Element_X"]),
        4: (
            "Quaternary",
            ["Element_A", "Element_B", "Element_C", "Element_D"],
        ),
    }

    label_keys_map = {
        2: ["A", "B"],
        3: ["R", "M", "X"],
        4: ["A", "B", "C", "D"],
    }

    custom_labels = {}
    for num_elements, (sheet, columns) in sheet_map.items():
        df = pd.read_excel(excel_path, sheet_name=sheet, engine="openpyxl")
        element_lists = [df[col].dropna().tolist() for col in columns]
        label_keys = label_keys_map[num_elements]
        custom_labels[num_elements] = {
            label: elements
            for label, elements in zip(label_keys, element_lists)
        }
    return custom_labels
