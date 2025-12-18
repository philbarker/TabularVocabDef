import pytest
from tvd2rdf import toLowerCamelCase


def test_toLowerCamelCase():
    assert toLowerCamelCase("URL") == "url"
    for ri in [
        "rangeIncludes",
        "Range includes",
        "Range-Includes",
        "range_includes",
        "Range_Includes",
        "range includes",
        "RANGE_INCLUDES",
    ]:
        assert toLowerCamelCase(ri) == "rangeIncludes"
