"""
 Test hello.yaml correctness

 File:         hellotest.py
 Created:      110718
"""

import yaml


with open('hello.yml') as f:
  l = yaml.load(f.read())
  print(yaml.dump(l,default_flow_style=False))


## EOF ##
