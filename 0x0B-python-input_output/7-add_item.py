#!/usr/bin/python3
"""Module that adds all arguments to a python list and then
   savethem to a file"""

from os import path
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if path.exists('add_item.json'):
    obj_fil = load_from_json_file('add_item.json')
else:
    obj_fil = []

for p in range(1, len(argv)):
    obj_fil.append(argv[p])

save_to_json_file(obj_fil, 'add_item.json')
