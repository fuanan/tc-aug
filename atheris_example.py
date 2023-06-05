import os
import sys

import atheris
from target_program import target_method_searchInsert
import logging


def gen_tc():
    os.environ['INVOKE_COUNT'] = '0'
    arglist1 = []
    arglist1.extend(sys.argv)
    l1 = ["-only_ascii=1", "-atheris_runs=1000", "./test_inputs/"]
    arglist1.extend(l1)
    runFuzz(arglist1, target_method_searchInsert)


def runFuzz(arglist, target_method):
    atheris.Setup(arglist, target_method)
    atheris.Fuzz()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='procedure.log', filemode='a')
    logging.info("1")
    gen_tc()
