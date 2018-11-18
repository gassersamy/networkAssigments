def to_int(message):
    if (message[0:2] == '0x'):
        return int(message[2:],16)
    elif (message[0:2] == '0b'):
        return int(message[2:],2)
    return int(message,10)