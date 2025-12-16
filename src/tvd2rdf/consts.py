from rdflib import RDF, RDFS, OWL, SDO, SKOS, DCTERMS

known_fields = [
    "type",  # maps to rdfs:type,
    "uri",  # maps to URIRef
    "label",  # maps to rdfs:label
    "comment",  # maps to rdfs:comment
    "usageNote",  # maps to skos:usageNote
    "domainIncludes",  # maps to sdo.domainIncludes
    "rangeIncludes",  # maps to sdo.rangeIncludes
    "definition",  # maps to skos:definition
    "notation",  # maps to skos:notation
    "relatedTerm",  # maps to object of a relationship statement
    "relationship",  # maps to predicate of a relationship statement
]

types_map = {
    "Property": RDF.Property,
    "Class": RDFS.Class,
    "Ontology": OWL.Ontology,
    "Concept Scheme": SKOS.ConceptScheme,
    "Concept": SKOS.Concept,
}

relationships_map = {
    "hasTopConcept": SKOS.hasTopConcept,
    "topConceptOf": SKOS.topConceptOf,
    "inScheme": SKOS.inScheme,
    "broader": SKOS.broader,
    "narrower": SKOS.narrower,
    "broadMatch": SKOS.broadMatch,
    "narrowMatch": SKOS.narrowMatch,
}

splitters = ",\n|;\n|\n|,|;"  # chars used to separate multiple entries in a cell.

serialization_order = [
    OWL.Ontology,
    RDFS.Class,
    RDF.Property,
    SKOS.ConceptScheme,
    SKOS.Concept,
]
