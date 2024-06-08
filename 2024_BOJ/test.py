def solve(N):
    MOD = 998244353

    # Convert N to string to find its length
    N_str = str(N)
    length_N = len(N_str)

    # Compute the initial value of repeated N as a large integer
    repeated_value = int(N_str * N)

    # Compute the result by taking modulo at each step to avoid overflow
    result = 0
    base = 1

    # Go through each digit in the repeated_value and compute modulo
    for char in reversed(N_str * N):
        result = (result + int(char) * base) % MOD
        base = (base * 10) % MOD

    return result


# Input
N = int(input())

# Output
print(solve(N))
