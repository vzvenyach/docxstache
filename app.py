#!/usr/bin/env python

from docx import Document
import re

def replace_field(run, field, repl):    
    field_str = "{{" + field + "}}"
    if field_str in run.text:
        try:
            run.text = re.sub(field_str, repl, run.text)
        except:
            raise
    return run

def replace_document(doc, kp):
    try:
        document = Document(docx=doc)
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                for key, value in kp.items():
                    run = replace_field(run, key, value)
        return document
    except:
        raise