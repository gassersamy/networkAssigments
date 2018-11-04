"""
    CRC Generator made by Network Geniuses team
"""
# ============   settings   ========================
POLY_NOMIAL = 0b11011

# ============ assignment functions ================

def generator (message):
    #input is in int form
    #TODO, return in int form message_with_remainder
    message_with_remainder=message
    return message_with_remainder

def verifier(message_with_remainder):
    # input will be in int form
    #TODO => decide to return 'OK' or 'Altered!'
    return 'OK'

def alter(message_with_remainder,bit_to_alter):
    # input will be in int form
    #TODO => alter the given bit (from right to left 0 indexed) and return altered message
    altered = message_with_remainder
    return altered

# ================ handling input ==================
def to_int(message):
    if (message[0:2] == '0x'):
        return int(message[2:],16)
    elif (message[0:2] == '0b'):
        return int(message[2:],2)
    return int(message,10)

user_note = "Kindly enter the message you wanna transmit\n"
user_note += "ex(1): 0b11001010\n"
user_note += "ex(2): 0xCA\n"
user_note += "ex(3): 202\n"

message = input(user_note)
message = to_int(message)

transmited = generator(message)
print("=======================================")
print("Transmited message will be: "+bin(transmited))
print("Verifier says: "+ verifier(transmited))

#could be changed to get the altered index from user
print ("Altering LSB ...")
altered = alter(transmited,0)
print("Altered message will be: "+bin(altered))
print("Verifier says: "+ verifier(altered))