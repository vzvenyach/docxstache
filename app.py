#!/usr/bin/env python

from docx import Document
import re

def replace_field(run, field, repl):    
    field_str = "{{" + field + "}}"
    if field_str in run.text:
        print field_str
        return re.sub(field_str, repl, run.text)
    else:
        return run.text

def replace_document(doc, kp):
    try:
        document = Document(docx=doc)
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                for key, value in kp.items():
                    run.text = replace_field(run, key, value)
        return document
    except:
        print "Invalid File Name"

import sys
import json

if len(sys.argv) < 2:
    print "Usage info here"
else:
    with open(sys.argv[2]) as f:
        o = json.load(f)
    d = replace_document(sys.argv[1], o)
    d.save(sys.argv[3])