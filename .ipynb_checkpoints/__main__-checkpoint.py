# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:19:01 2020

@author: Michael K. Bergman
"""

from cowpoke.config import * 
from owlready2 import *
import csv

world = World()

kb_src = master_deck.get('kb_src')                         # we get the build setting from config.py

if kb_src is None:
    kb_src = 'standard'
elif kb_src is 'extract':
    kbpedia = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/ontologies/kbpedia_reference_concepts.owl'
    kko_file = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/stubs/kko.owl'
elif kb_src is 'full':
    kb_src = 'start'    
elif kb_src == 'sandbox':
    kbpedia = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/ontologies/kbpedia_reference_concepts.owl'
    kko_file = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/ontologies/kko.owl'
elif kb_src == 'standard':
    kbpedia = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/ontologies/kbpedia_reference_concepts.owl'
    kko_file = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/stubs/kko.owl'
elif kb_src == 'start':
    kbpedia = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/stubs/kbpedia_rc_stub.owl'
    kko_file = '/Users/lawrence/Documents/GitHub/CWPK/sandbox/builds/stubs/kko.owl'
else:
    print('You have entered an inaccurate source parameter for the build.')
skos_file = 'http://www.w3.org/2004/02/skos/core'


kb = world.get_ontology(kbpedia).load()
rc = kb.get_namespace('http://kbpedia.org/kko/rc/')               

skos = world.get_ontology(skos_file).load()
kb.imported_ontologies.append(skos)
core = world.get_namespace('http://www.w3.org/2004/02/skos/core#')

kko = world.get_ontology(kko_file).load()
kb.imported_ontologies.append(kko)
kko = kb.get_namespace('http://kbpedia.org/ontologies/kko#')


def render_using_iri(entity):
    return entity.iri

def render_using_label(entity):
    return entity.label.first() or entity.name    