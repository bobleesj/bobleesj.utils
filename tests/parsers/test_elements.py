from bobleesj.utils.parsers.elements import get_custom_labels_from_excel

def test_get_custom_labels_from_excel(custom_label_excel_path):
    actual_custom_label = get_custom_labels_from_excel(custom_label_excel_path)
    assert actual_custom_label == {
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
