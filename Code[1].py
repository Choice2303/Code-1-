import itertools
import secrets 
import time
from array import *
import random

def generateOptions(length_of_bits):
    print("|Number of keys|\n")
    for a in length_of_bits:
            opt = (2**a)
            print(a,"bits:", opt, "\n")

def generateKeys(length_of_bits, voc_keys):
    print("\n|Gen keys|\n")
    for a in length_of_bits:
        key = random.getrandbits(a)
        voc_keys[int(key)] = key
        print("==========",a, "-> key ==========\n", key, "\n=========================================\n")
            
def brute_force(voc_keys):
    limit = 2**4096
    start = time.monotonic_ns()
    for a in range(limit):
        search_key = voc_keys.get(a, False)
        if search_key:
            finish=time.monotonic_ns() 
            duration = finish -  start
            print("Key ", a,"found -> ",duration//1000000, "ms")
            
keys = dict()         
bits = array('i', [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])

generateOptions(bits)
generateKeys(bits, keys)
brute_force(keys) 
