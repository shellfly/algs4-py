"""
 *  Execution:    python binarydump.py n < file
 *  Data file:    https://introcs.cs.princeton.edu/stdlib/abra.txt
 *  
 *  Reads in a binary file and writes out the bits, n per line.
 *
 *  % more abra.txt 
 *  ABRACADABRA!
 *
 *  % python binarydump.py 16 < abra.txt
 *  0100000101000010
 *  0101001001000001
 *  0100001101000001
 *  0100010001000001
 *  0100001001010010
 *  0100000100100001
 *  96 bits
 *
"""

import sys
from algs4.binarystdin import BinaryStdin

bits_per_line = 16
if len(sys.argv) == 2:
    bits_per_line = int(sys.argv[1])
count = 0
while not BinaryStdin.is_empty():
    if bits_per_line == 0:
        BinaryStdin.read_bool()
        continue
    elif count != 0 and count % bits_per_line == 0:
        print()
    if BinaryStdin.read_bool():
        print(1, end="")
    else:
        print(0, end="")
    count += 1
if bits_per_line != 0:
    print()
print(count, "bits")
