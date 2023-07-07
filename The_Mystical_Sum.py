# Problem: The Mystical Sum
# You are given a positive integer N. Your task is to find the sum of all numbers between 1 and N (exclusive) that are divisible by a prime number.
# Write a Python program that takes a positive integer N as input and calculates the sum of all numbers between 1 and N (exclusive) that are divisible by a prime number.


# Sample Input: 10
# Sample Output: 17

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mystical_sum(N):
    prime_divisors = set()
    sum_result = 0
    for num in range(1, N):
        if any(num % prime == 0 for prime in prime_divisors):
            continue
        if is_prime(num):
            prime_divisors.add(num)
            sum_result += num
    return sum_result

# Prompt the user for input
N = int(input())

# Calculate the mystical sum
result = mystical_sum(N)

# Print the result
print(result)

        


