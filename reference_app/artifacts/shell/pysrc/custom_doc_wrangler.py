__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import os
import sys
import traceback
import uuid

# This is a shell class for customers to create their own wrangler logic.
# Implement the "wrangle(self, doc)" method to modify doc as necessary; 
# it is a parsed dict from a mongoexport line.  Optionally use the mappings
# dict passed to the constructor method.  See the default implementation
# of class StandardDocumentWrangler in file standard_doc_wrangler.py

class CustomDocumentWrangler(object):

    def __init__(self, mappings):
        self.mappings = mappings

    def wrangle(self, doc):
        self.wrangle_pk(doc)
        self.wrangle_doctype(doc)
        self.wrangle_excludes(doc)
        self.wrangle_some_custom_thing(doc)
        self.wrangle_something_else(doc)

    def wrangle_pk(self, doc):
        pass

    def wrangle_doctype(self, doc):
        pass

    def wrangle_excludes(self, doc):
        pass

    def wrangle_some_custom_thing(self, doc):
        pass

    def wrangle_something_else(self, doc):
        pass
