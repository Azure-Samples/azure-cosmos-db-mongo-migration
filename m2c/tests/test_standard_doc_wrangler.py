__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "July 2021"

import json
import os
import time
import pytest

from pysrc.standard_doc_wrangler import StandardDocumentWrangler

# This file implements unit tests of class StandardDocumentWrangler,
# using the pytest framework.

def test_no_wrangling():
    mapping = noop_airports_mapping()
    wrangler = StandardDocumentWrangler(mapping)
    doc = clt_airport_mongoexport_doc()
    json1 = json.dumps(doc, separators=(',', ':'))

    wrangler.wrangle(doc)
    json2 = json.dumps(doc, separators=(',', ':'))

    assert(json1 == json2)

def test_complete_wrangling():
    mapping = airports_mapping()
    wrangler = StandardDocumentWrangler(mapping)
    doc = clt_airport_mongoexport_doc()
    json1 = json.dumps(doc, separators=(',', ':'))
    assert(has_key(doc, 'pk') == False)
    assert(has_key(doc, 'doctype') == False)
    assert(has_key(doc, 'cname') == False)
    assert(has_key(doc, 'e') == False)
    assert(has_key(doc, 'u') == False)
    assert(has_key(doc, 'migrated') == False)
    assert(has_key(doc, 'airport_id') == True)
    assert(has_key(doc, 'source') == True)
    assert(has_key(doc, 'type') == True)
    assert(doc['airport_id'] == '3876')
    assert(('60bbb4c41e1a91cb40f7241d' in json1) == True)

    wrangler.wrangle(doc)
    json2 = json.dumps(doc, separators=(',', ':'))
    print(json2)

    assert(doc['pk'] == 'Charlotte Douglas International Airport-xxx')
    assert(doc['doctype'] == 'x-3876-airports')
    assert(doc['cname'] == 'airports')
    assert(has_key(doc, 'airport_id') == False)
    assert(has_key(doc, 'source') == False)
    assert(has_key(doc, 'type') == False)
    assert(has_key(doc, 'e') == True)
    assert(has_key(doc, 'u') == True)
    assert(has_key(doc, 'migrated') == True)
    assert(doc['migrated'] == 'yes')
    assert(('60bbb4c41e1a91cb40f7241d' in json2) == False)

def noop_airports_mapping():
    j = """
    {
      "name": "airports",
      "mapping": {
        "target_dbname": "travel",
        "target_container": "airports",
        "wrangling_algorithm": "standard",
        "pk_name": "pk",
        "pk_logic": [],
        "pk_sep": "-",
        "doctype_name": "doctype",
        "doctype_logic": [],
        "doctype_sep": "-",
        "additions": [],
        "excludes": []
      }
    }
    """
    return json.loads(j.strip())

def airports_mapping():
    j = """
    {
      "name": "airports",
      "mapping": {
        "target_dbname": "travel",
        "target_container": "airports",
        "wrangling_algorithm": "standard",
        "pk_name": "pk",
        "pk_logic": [
          [
            "attribute",
            "name"
          ],
          [
            "literal",
            "xxx"
          ],
          [
            "attribute",
            "oops_not_there"
          ]
        ],
        "pk_sep": "-",
        "doctype_name": "doctype",
        "doctype_logic": [
          [
            "literal",
            "x"
          ],
          [
            "attribute",
            "oops_not_there"
          ],
          [
            "attribute",
            "airport_id"
          ],
          [
            "dynamic",
            "source_cname"
          ]               
        ],
        "doctype_sep": "-",
        "additions": [
            [ "dynamic", "cname", "source_cname" ],
            [ "dynamic", "e", "epoch" ],
            [ "dynamic", "u", "uuid" ],
            [ "dynamic", "_id", "oid" ],
            [ "literal", "migrated", "yes" ]
        ],
        "excludes": [ "airport_id", "source", "type" ]
      }
    }
    """
    return json.loads(j.strip())

def clt_airport_mongoexport_doc():
    return json.loads('{"_id":{"$oid":"60bbb4c41e1a91cb40f7241d"},"airport_id":"3876","name":"Charlotte Douglas International Airport","city":"Charlotte","country":"United States","iata_code":"CLT","icao_code":"KCLT","latitude":"35.2140007019043","longitude":"-80.94309997558594","altitude":"748","timezone_num":"-5","dst":"A","timezone_code":"America/New_York","type":"airport","source":"OurAirports"}')

def has_key(doc, key):
    if key in doc.keys():
        return True
    else:
        return False 
