import pytest
from tvd2rdf._utils import toLowerCamelCase, load_config, convert_namespace, str2URIRef
from rdflib import URIRef, SDO, RDF, RDFS

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

def test_load_config():
    config = load_config()
    assert config["relationships map"]["hasTopConcept"] == 'skos:hasTopConcept'
    assert config["types map"]["Property"] == "rdf:Property"
    assert config["namespaces"]["dcterms"] == "http://purl.org/dc/terms/"
    
def test_convert_namespace():
    ns = convert_namespace("ex:", "http://example.org/")
    print(ns)
    assert ns == {"ex": "http://example.org/"}

def test_str2URIRef():
    ns = {"rdfs": "http://www.w3.org/2000/01/rdf-schema#"}
    string = "rdfs:label"
    uri = str2URIRef(ns, string)
    assert uri == RDFS.label
    ns = {"base": "https://schema.org/"}
    string = "name"
    uri = str2URIRef(ns, string)
    assert uri == SDO.name
    string = "https://schema.org/description"
    ns = {}
    uri = str2URIRef(ns, string)
    assert uri == URIRef(string)
    uri = str2URIRef({}, "name")
    assert uri == URIRef("http://example.org/name")
    ns = {"base": "http://example.org/terms#"}
    uri = str2URIRef(ns, "#name")  # make sure the extra # is stripped
    assert uri == URIRef("http://example.org/terms#name")
    with pytest.raises(TypeError) as e:
        uri = str2URIRef([], "name")
    assert str(e.value) == "Namespaces should be a dictionary."
    with pytest.raises(TypeError) as e:
        uri = str2URIRef({}, 42)
    assert str(e.value) == "Value to convert should be a non-empty string."
    with pytest.raises(TypeError) as e:
        uri = str2URIRef({}, "")
    assert str(e.value) == "Value to convert should be a non-empty string."
    with pytest.raises(ValueError) as e:
        uri = str2URIRef({}, "ns:name")
    assert str(e.value) == "Prefix ns not in namespace list."