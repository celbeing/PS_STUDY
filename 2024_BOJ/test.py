import os
import sys



def main():
    input_num = int(input())
    prime_list = find_prime(input_num)
    check_num  = 1
    for prime_at in prime_list:
        check_num *= prime_at
    print("[%s] input_num=%d, check_num=%d" % (input_num == check_num, input_num, check_num))
    print("%s" % prime_list)

main()