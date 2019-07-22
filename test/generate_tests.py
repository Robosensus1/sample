# -*- coding: utf-8 -*-
""" Generate intergration tests for a bot written with RASA NLU
The program extracts intents and data used for model training
to generate tests.
"""

import os
import re

FILENAME = "./nlu.md"
URL = "http://localhost:5000/parse"


def generate():

    print ("import requests")


    with open(FILENAME, 'r') as file_descriptor:
        current_intent = None
        sentence_idx = 0
        
        for line in [ x.strip() for x in  file_descriptor.readlines() ]:

            if line.startswith('##'):
                current_intent = line.split(':')[1]
                sentence_idx = 0
            elif current_intent and line.startswith('-'):
                sentence = line[2:]
                test_template(current_intent, sentence, sentence_idx)
                sentence_idx += 1
                
        file_descriptor.close()


def test_template(intent, sentence, sentence_idx):
    print ("def test_integration_{0}_{1}():".format(intent, sentence_idx))
    print(
        '\tr = requests.post(\"' +
        URL + 
        '\",' +
        'json = {\"q\":\"' +
        sentence + 
        '\", \"project\":\"current\", \"model\":\"nlu\"})'
    )

    print("\tassert r.status_code == 200")
    print("\tassert 'intent' in r.json()")
    print("\tassert r.json()['intent'].get('name') is not None")
    print("\tassert r.json()['intent']['name'] == '{}'".format(intent))


if __name__ == '__main__':
    generate()
    


