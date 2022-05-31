import sys
from rdflib import Graph, Literal, RDF, URIRef, Namespace, BNode
from rdflib.namespace import FOAF, XSD, DCTERMS, SDO, RDF
import json
import pandas as pd
import numpy as np
import re
import rdflib

if __name__ == "__main__":

    query = sys.argv[1]
    tokenized_query = query.split(" ")
    query = """
    prefix NameSpace: <http://www.lessurligneurs.eu/ontologies/2022/surligneurs-ontology#>
    SELECT ?b
    WHERE {
        ?a NameSpace:title ?b .\n"""

    for term in tokenized_query:
        relatedEntity = "?a NameSpace:relatedEntity NameSpace:"+term+".\n"
        query = query + relatedEntity
    query = query + "}"

    
    g = rdflib.Graph()
    g.parse("newRDF-filev3.rdf")
    results = g.query(query)

    print("\n============QUERY RESULTS===============\n")
    if(len(results)>0):
        print(f"We Have {len(results)} results")
        print("The results are:")
        for row in results:
            print(row.b)
            print()
    else:
        print("No Results")


