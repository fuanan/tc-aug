import os

import atheris
import inspect
import fnmatch
import importlib
import sys


fuzz_temp_dir = "fuzz_temp"
programs = fnmatch.filter(os.listdir(fuzz_temp_dir), '*code.py')
program = programs[0]

stem, suffix = os.path.splitext(program)
module_name = f'{fuzz_temp_dir}.{stem}'
target = importlib.import_module(module_name)
if module_name in sys.modules:
    print(f'{module_name} find!')

members = inspect.getmembers(target, inspect.isfunction)
func_name = 'coutPairs'
fun = None
for name, f in members:
    if name == func_name:
        fun = f
        break

signature = inspect.signature(fun)

for para_name, para in signature.parameters.items():
    if para.annotation != inspect.Parameter.empty:
        print(f"Parameter name: {para_name}")
        print(f"Parameter type: {para.annotation}")

# 卸载方法
del sys.modules[f'{fuzz_temp_dir}.{stem}']
if module_name not in sys.modules:
    print(f'{module_name} deleted!')


target = importlib.import_module("fuzz_temp.print_module1")
target.print_content()

del sys.modules["fuzz_temp.print_module1"]
print("1")

target = importlib.import_module("fuzz_temp.print_module1")
target.print_content()

del sys.modules["fuzz_temp.print_module1"]

