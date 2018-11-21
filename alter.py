import sys
from to_int import *

def alter(message_with_remainder,bit_to_alter):
    # input will be in int form
    #TODO => alter the given bit (from left to right 1 indexed) and return altered message
    index = bit_to_alter-1
    m_string = bin(message_with_remainder).split('0b')[1]
    bit = m_string[index]
    not_bit = '0' if (bit=='1') else '1'
    altered = m_string[0:index]+not_bit+m_string[index+1:]
    return altered
    
bit_to_change = to_int(sys.argv[1])
trans_str = input() 
POLY_STR = input()

trans_msg = to_int('0b'+trans_str)
POLY_NOMIAL = to_int('0b'+POLY_STR)
trans_altered = alter(trans_msg,bit_to_change)

print(trans_altered)
print(POLY_STR)