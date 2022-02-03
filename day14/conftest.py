import pytest


@pytest.fixture
def sample_data():
    return (
        "NNCB",
        {
            "BB": "N",
            "BC": "B",
            "BH": "H",
            "BN": "B",
            "CB": "H",
            "CC": "N",
            "CH": "B",
            "CN": "C",
            "HB": "C",
            "HC": "B",
            "HH": "N",
            "HN": "C",
            "NB": "B",
            "NC": "B",
            "NH": "C",
            "NN": "C",
        },
    )
