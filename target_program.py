import atheris
import random
import logging
import os
import sys
import string


@atheris.instrument_func
def target_method(data):  # Our entry point
    if len(data) != 8:
        return
    if chr(data[0]) == "d":
        if chr(data[1]) == "e":
            if chr(data[2]) == "a":
                if chr(data[3]) == "d":
                    if chr(data[4]) == "b":
                        if chr(data[5]) == "e":
                            if chr(data[6]) == "e":
                                if chr(data[7]) == "f":
                                    a = 1


def generate_random_string(length):
    letters = string.ascii_letters  # 所有大小写字母
    result = ''.join(random.choice(letters) for _ in range(length))
    return result


def target_method_searchInsert(input_bytes):
    logging.error(input_bytes)
    fdp1 = atheris.FuzzedDataProvider(input_bytes)
    list_1 = fdp1.ConsumeIntListInRange(random.randint(1, 100), 0, sys.maxsize)
    fdp2 = atheris.FuzzedDataProvider(os.urandom(random.randint(1, 100)))
    int_1 = fdp2.ConsumeIntInRange(1, sys.maxsize)
    searchInsert(list_1, int_1)
    i = int(os.getenv('INVOKE_COUNT'))
    i = i + 1
    os.environ['INVOKE_COUNT'] = str(i)
    if len(list_1) == 0:
        l_str = ""
    else:
        l_str = ",".join([str(element) for element in list_1])
    logging.info(f"i={i},[{l_str}],{int_1}")


@atheris.instrument_func
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    return left
