#!/usr/bin/env python
import app
import sys
import json

if len(sys.argv) < 2:
    print "Usage info here"
else:
    with open(sys.argv[2]) as f:
        o = json.load(f)
    d = app.replace_document(sys.argv[1], o)
    d.save(sys.argv[3])