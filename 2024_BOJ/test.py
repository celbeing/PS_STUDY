import itertools

def validate_input_2(str):
    key = "TSFHHABP"
    hint = "\\BD_OBNZ"

    prv = 0
    for i in range(8):
        prv = ((prv << 1) ^ ord(str[i])) & 31
        if chr(prv + ord('A')) != key[i]:
            return False

    decrypted_str = ""
    for i in range(8):
        decrypted_str += chr(ord(str[i]) ^ (ord(hint[i]) & 31))
    print(decrypted_str)
    return True

def brute_force():
    found_valid = False
    for combination in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=8):
        candidate = ''.join(combination)
        if validate_input_2(candidate):
            print("Valid input found:", candidate)
            found_valid = True
            return
        else:
            print("Failed combination:", candidate)

brute_force()
