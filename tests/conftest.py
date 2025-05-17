import pytest

from bobleesj.utils.sources.oliynyk import get_oliynyk_CAF_data


@pytest.fixture
def CAF_oliynyk_db():
    return get_oliynyk_CAF_data()
