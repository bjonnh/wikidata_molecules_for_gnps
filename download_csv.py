#!/usr/bin/env python3

import requests
import csv

SPARQL_SERVER = 'https://query.wikidata.org/sparql'
QUERY = """
SELECT * WHERE {
  ?s wdt:P235 ?inchikey;
     wdt:P233 ?smiles.
  } 
"""
OUTPUT = 'output.tsv'

with open(OUTPUT, 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['smiles', 'inchikey', 'wikidata_page'])
    for i in requests.post(SPARQL_SERVER,
                           params={"query": QUERY},
                           headers={'accept': 'application/sparql-results+json'}).json()["results"]["bindings"]:
        tsv_writer.writerow([i['smiles']['value'], i['inchikey']['value'], i['s']['value']])
