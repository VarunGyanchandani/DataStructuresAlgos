def findKthBit(n: int, k: int) -> str:
    def generate_string(n):
        # Base case
        if n == 1:
            return '0'

        # Recursive case
        prev_str = generate_string(n - 1)
        inverted = ''.join('1' if c == '0' else '0' for c in prev_str)
        reversed_str = inverted[::-1]
        return prev_str + '1' + reversed_str

    # Generate the nth binary string
    binary_str = generate_string(n)

    # Return the kth bit
    return binary_str[k - 1]

print(findKthBit(3,1))
print(findKthBit(4,11))