__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import json
import os
import pprint
import sys
import time
import uuid

import arrow
import jinja2

from operator import itemgetter
from pysrc.config import Config
from pysrc.manifest import Manifest

# Class DocGenerator was used to generate the initial set of documentation
# markdown files.

class DocGenerator(object):    

    def __init__(self):
        pass

    def generate(self):
        structure = self.documentation_structure()

        # Generate the List of Pages for the main README.md file to copy-and-paste
        for page_idx, page in enumerate(structure):
            title = '{} - {}'.format(page['num'], page['name'])
            print('- [{}]({})'.format(title, page['filename']))

        # Generate the individual markdown pages
        for page_idx, page in enumerate(structure):
            print(json.dumps(page, sort_keys=False, indent=2))
            template_data = page
            template_name = 'doc_page.txt'
            outfile = 'tmp/{}'.format(page['filename'])
            self.render_template(template_name, template_data, outfile)

    def documentation_structure(self):
        lines, structure = list(), list()
        lines.append('Purpose')
        lines.append('Project Implementation,MongoDB,mongoexport,Python3,Jinja2 templates,Shell Scripts,Azure Storage,Azure Data Factory,Azure CosmosDB')
        lines.append('Reference Application,Reference Databases,Reference Artifacts')
        lines.append('Development Computer Setup,Software Requirements,Environment Variables,Python Virtual Environment')
        lines.append('Initial Customer Edits,env.sh,Databases List')
        lines.append('Generate Initial Scripts')
        lines.append('Extract Source Database Metadata,Sample')
        lines.append('Generate Mapping Files,Sample')
        lines.append('Edit the Mapping Files,Source to Target Mappings,Wrangling/Transformations')
        lines.append('Generate the Manifest,Excel,JSON Sample')
        lines.append('Generate Artifacts,mongoexport Scripts,Storage Container Scripts,File Upload Scripts,Wrangling Scripts,Create Cosmos Database and Containers scripts,Cosmos/Mongo Index Files,ADF JSON Artifacts,replicate_scripts.sh')
        lines.append('Provision Azure Resources,Storage,Virtual Machine,Azure Data Factory,CosmosDB with Mongo API')
        lines.append('Create the Azure Storage Containers,Execute the Generated Scripts')
        lines.append('Create the CosmosDB Target Databases and Containers,Execute the Generated Scripts')
        lines.append('CosmosDB Container Indexing,Edit the Cosmos/Mongo Index Files,Execute the Generated Scripts')
        lines.append('ADF Setup with Git Source Control,Github Repo Setup,ADF Linked Services, ADF Datasets, ADF Pipelines')
        lines.append('Execute Migration,mongoexports,Wrangling for ADF,Execute ADF Pipelines,Verify')
        lines.append('Roadmap')

        for line_idx, line in enumerate(lines):
            structure.append(self.page(line_idx, line))
        return structure

    def page(self, line_idx, csv_line):
        tokens = csv_line.split(',')
        page_num = '{:02d}'.format(line_idx)
        page_name = tokens[0]
        page = {}
        page['num'] = page_num
        page['name'] = page_name
        page['filename'] = '{}_{}.md'.format(page_num, page_name).lower().replace(' ','_')
        page['sections'] = list()
        for idx, tok in enumerate(tokens):
            if idx > 0:
                page['sections'].append(tok.strip())
        return page

    def timestamp(self):
        return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss UTC')

    def render_template(self, template_name, template_data, outfile):
        t = self.get_template(os.getcwd(), template_name)
        s = t.render(template_data)
        self.write(outfile, s)

    def get_template(self, root_dir, name):
        filename = 'templates/{}'.format(name)
        return self.get_jinja2_env(root_dir).get_template(filename)

    def get_jinja2_env(self, root_dir):
        return jinja2.Environment(
            loader = jinja2.FileSystemLoader(
                root_dir), autoescape=True)

    def write(self, outfile, s, verbose=True):
        with open(outfile, 'w') as f:
            f.write(s)
            if verbose:
                print('file written: {}'.format(outfile))
