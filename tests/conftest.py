import pytest

from bobleesj.utils.sources.oliynyk import get_oliynyk_CAF_data


@pytest.fixture
def CAF_oliynyk_db():
    # 20250516 - deleted Tc, Pm and Hg since some properties are not available
    return get_oliynyk_CAF_data()
