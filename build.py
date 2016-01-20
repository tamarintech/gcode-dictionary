#!/usr/bin/env python

import json
import os

gcode_dictionary = {}

for deffile in os.listdir('files/'):
  if deffile.endswith(".json"):
    with open('files/' + deffile) as f:
      gcode_definition = json.load(f)
      gcode_dictionary[gcode_definition['code']] = gcode_definition

with open('gcode_dictionary.json', 'w') as f:
  f.write(json.dumps(gcode_dictionary,
                     sort_keys=True,
                     indent=2, 
                     separators=(',', ': ')))