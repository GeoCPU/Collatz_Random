import random

def generate_random_big_number(max_digits=1000):
    """
    Generates a random integer with digit length chosen uniformly from 1 to max_digits.
    """
    digits = random.randint(1, max_digits)
    if digits == 1:
        return random.randint(1, 9)
    lower_bound = 10 ** (digits - 1)
    upper_bound = (10 ** digits) - 1
    return random.randint(lower_bound, upper_bound)

def collatz_check(n, max_steps=100_000_000):
    steps = 0
    visited = set()
    original = n

    print(f"\n[START] Starting Collatz sequence for number:\n{original} ({len(str(original))} digits)")

    while n != 1 and steps < max_steps:
        if n in visited:
            print(f"[!] Loop detected! Starting number was:\n{original}")
            return False
        visited.add(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

        if steps % 1_000_000 == 0:
            print(f"[...] {steps:,} steps so far for number:\n{original}")

    if n == 1:
        print(f"[✓] Reached 1 in {steps:,} steps. Starting number was:\n{original}\n")
        return True
    else:
        print(f"[X] Did NOT reach 1 in {max_steps:,} steps. Starting number was:\n{original}\n")
        with open("collatz_fails.txt", "a") as f:
            f.write(f"{original} did not reach 1 in {max_steps} steps\n")
        return False

if __name__ == "__main__":
    max_digits = 1000

    while True:
        n = generate_random_big_number(max_digits)
        collatz_check(n)
