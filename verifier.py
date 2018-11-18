import sys
from gen import generator
from to_int import *

def verifier(message_with_remainder, POLY_NOMIAL):
    # input will be in int form
    #TODO => decide to return 'Correct' or 'Altered!'
    r_bit_len = POLY_NOMIAL.bit_length() - 1
    base_msg = message_with_remainder >> r_bit_len
    base_after_gen = generator(base_msg,POLY_NOMIAL)
    if base_after_gen != message_with_remainder:
        return 'Message is Altered!'
    return 'Message is Correct :)'

trans_str = input() if len(sys.argv)==1 else sys.argv[1]
POLY_NOMIAL = input() if len(sys.argv)==1 else sys.argv[2]

trans_msg = to_int('0b'+trans_str)
POLY_NOMIAL = to_int('0b'+POLY_NOMIAL)

response = verifier(trans_msg,POLY_NOMIAL)
print("Transmitted Message: "+trans_str)
print(response)