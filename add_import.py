import os
import fnmatch


fuzz_temp_dir = "fuzz_temp"
programs = fnmatch.filter(os.listdir(fuzz_temp_dir), '*.py')
program = programs[0]

imports = '\n'.join(['from typing import *', 'from math import *',
                     'from collections import *', 'from itertools import *',
                     'from functools import *', 'import collections',
                     'import random', 'from operator import *',
                     'import sortedcontainers', 'from sortedcontainers import *'])


with open(f'{fuzz_temp_dir}/{program}', 'r') as file:
    content = file.read()
    new_content = imports + '\n\n\n' + content

with open(f'{fuzz_temp_dir}/{program}', 'w+') as fw:
    fw.write(new_content)
