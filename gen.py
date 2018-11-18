import sys
from to_int import *

def generator (message, POLY_NOMIAL):
    #input is in int form
    #TODO, return in int form message_with_remainder
    r_bit_len = POLY_NOMIAL.bit_length() - 1
    m_bit_len = message.bit_length()
    temp_bit_len = m_bit_len
    
    # adding zeros to poly nomial to be able to xor
    diff = m_bit_len - (r_bit_len+1)
    extended_poly = POLY_NOMIAL * (2**diff)
    
    #initially remainder = binary of msg after removing 0b
    rem_str = bin(message).split("0b")[1]
    while temp_bit_len > 0 :
        #if MSB is 1
        if(rem_str[0]=='1'):
            #xor
            rem_int = to_int('0b'+rem_str) ^ extended_poly
            rem_str = bin(rem_int).split("0b")[1].zfill(m_bit_len)
        #shifting_left
        rem_str = rem_str[1:]+'0'
        temp_bit_len -= 1
    #xor is done, lets remove the right zeros we added befroe
    remainder = to_int("0b"+rem_str[0:r_bit_len])

    #putting reaminder besides base msg (if msg = 111 & rem = 111, => trans = 0b111000 + 0b111)
    #note 0b1000 = 1 * 2 to the power 3 = (8), so:
    message_with_remainder= (message* (2**r_bit_len) ) + remainder
    return message_with_remainder

def main():
    argc = len(sys.argv)
    msg=''
    POLY_NOMIAL = ''

    if (argc > 1):
        msg = sys.argv[1]
        POLY_NOMIAL = sys.argv[2]
    else:
        msg = input()
        POLY_NOMIAL = input()


    POLY_STR = POLY_NOMIAL
    msg = to_int('0b'+msg)
    POLY_NOMIAL = to_int('0b'+POLY_NOMIAL)

    transmited = generator(msg,POLY_NOMIAL)
    transmited_str = bin(transmited).split('0b')[1]
    print(transmited_str)
    print(POLY_STR)

if __name__ == "__main__":
    main()