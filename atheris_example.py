import os
import sys

import atheris
from target_program import target_method


def gen_tc():
    arglist1 = []
    arglist1.extend(sys.argv)
    l1 = ["-only_ascii=1", "-atheris_runs=10000", "./test_inputs/"]
    arglist1.extend(l1)
    runFuzz(arglist1, target_method)
    ret = os.system('chmod -R 777 test_inputs')
    # l2 = ["-merge=1", "./final_test_inputs/", "./test_inputs/"]
    # arglist2 = []
    # arglist2.extend(sys.argv)
    # arglist2.extend(l2)
    # runFuzz(arglist2, target_method)


def runFuzz(arglist, target_method):
    atheris.Setup(arglist, target_method)
    atheris.Fuzz()


if __name__ == "__main__":
    gen_tc()
